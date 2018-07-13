# 番外篇-为啥是BGR而不是RGB ?

我们当下普遍使用的是`RGB`格式, 但是为什么`cv2`返回的数据结构是`BGR`格式的呢?

这个问题, 跟之前阿凯提到的`cv2` 的问题一样, 同样困扰了我. 

在这篇文章中, 阿凯获得了答案, 早前`windows`下, 不管是摄像头制造者 ,还是软件开发者, 当时流行的都是`BGR` 格式的数据结构. 后面`RBG` 格式才逐渐流行, 所以这个是`opencv`在发展过程中的历史遗留问题. 

[Learn OpenCV - Why does OpenCV use BGR color format ?](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/)

> The reason the early developers at OpenCV chose BGR color format is that back then BGR color format was popular among camera manufacturers and software providers. E.g. in Windows, when specifying color value using COLORREF they use the BGR format 0x00bbggrr.
> BGR was a choice made for historical reasons and now we have to live with it. In other words, BGR is the horse’s ass in OpenCV.