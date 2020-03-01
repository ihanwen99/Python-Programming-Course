# -*- coding: utf-8 -*-

import cv2
import dlib


def add_hat(img, hat):
    # 分离图片的rgba通道，合成rgb三通道帽子图，a通道作为mask后面使用
    r, g, b, a = cv2.split(hat)
    rgb_hat = cv2.merge((r, g, b))

    cv2.imwrite("hat_alpha.png", a)

    # dlib正脸检测器
    detector = dlib.get_frontal_face_detector()
    dets = detector(img, 1)

    # dlib人脸关键点预测器
    predictor_path = "shape_predictor_5_face_landmarks.dat"
    predictor = dlib.shape_predictor(predictor_path)

    # 如果检测到人脸
    if len(dets) > 0:
        for i in dets:
            x, y, w, h = i.left(), i.top(), i.right() - i.left(), i.bottom() - i.top()
            shape = predictor(img, i)

            # 选取左右眼眼角的点
            point1 = shape.part(0)
            point2 = shape.part(2)

            # 求两点中心
            eyes_center = ((point1.x + point2.x) // 2, (point1.y + point2.y) // 2)

            #  根据人脸大小调整帽子大小
            #  factor手工放缩因子
            factor = 1
            resized_hat_h = int(round(rgb_hat.shape[0] * h / rgb_hat.shape[1] * factor))
            resized_hat_w = int(round(rgb_hat.shape[1] * w / rgb_hat.shape[1] * factor))
            # print(resized_hat_h, resized_hat_w)
            # print(rgb_hat.shape[1], rgb_hat.shape[0])

            if resized_hat_h > y:
                resized_hat_h = y - 1

            # 根据上面获取的大小调整帽子的大小
            resized_hat = cv2.resize(rgb_hat, (resized_hat_w, resized_hat_h))

            # alpha通道作为mask
            mask = cv2.resize(a, (resized_hat_w, resized_hat_h))
            # cv2.imshow("mask",mask)
            mask_inv = cv2.bitwise_not(mask)
            mask_inv = cv2.merge((mask_inv, mask_inv, mask_inv))
            cv2.imshow("mask_inv", mask_inv)

            # 帽子相对与人脸框上线的偏移量-对于我们的帽子优化一下为0
            dh = 0
            dw = 0

            # 原图感兴趣的区域(ROI)
            # //4 <- 4 根据图片来选取，可以自由切换帽子在头部的比例
            bg_roi = img[y + dh - resized_hat_h:y + dh,
                     (eyes_center[0] - resized_hat_w // 4):(eyes_center[0] + resized_hat_w // 4 * 3)]

            # 原图ROI中提取放帽子的区域
            bg_roi = bg_roi.astype(float)
            alpha = mask_inv.astype(float) / 255

            # 相乘之前保证两者大小一致(round)
            alpha = cv2.resize(alpha, (bg_roi.shape[1], bg_roi.shape[0]))
            bg = cv2.multiply(alpha, bg_roi)
            bg = bg.astype('uint8')

            cv2.imwrite("bg.jpg", bg)

            # 提取帽子区域
            hat = cv2.bitwise_and(resized_hat, resized_hat, mask=mask)
            cv2.imwrite("hat.jpg", hat)

            # 相加之前保证两者大小一致(round)
            hat = cv2.resize(hat, (bg_roi.shape[1], bg_roi.shape[0]))
            # 两个ROI区域相加
            add_hat = cv2.add(bg, hat)

            # 把添加好帽子的区域放回原图
            img[y + dh - resized_hat_h:y + dh,
            (eyes_center[0] - resized_hat_w // 4):(eyes_center[0] + resized_hat_w // 4 * 3)] = add_hat

            return img


if __name__ == '__main__':
    img = cv2.imread("img.jpg")
    cv2.imshow("Raw input", img)
    hat = cv2.imread("hat.png", -1)
    output = add_hat(img, hat)

    cv2.imshow("Final Output", output)
    cv2.waitKey(0)
    cv2.imwrite("outputHat.jpg", output)
