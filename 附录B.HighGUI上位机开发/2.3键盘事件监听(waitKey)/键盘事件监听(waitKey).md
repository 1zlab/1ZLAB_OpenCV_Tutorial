# 键盘事件的监听(waitKey)

接下来我们再讲一下opencv中一个键盘事件监听函数`waitKey`

```
cv2.waitKey(delay_ms)
```



这个函数其实有两个功能。 

1. 等待一个按键事件的发生
2. 延时delay_ms个毫秒



它的逻辑是这样的， 如果过了n个ms仍然也没等到有按键事件发生， 就继续执行下面的函数， 所以变相等于延时（delay）。



**注意 ， 这个函数只有在当前至少有一个窗口是激活状态下， 才会生效**

换句话说， 如果你在这期间， 点开了另外一个无关窗口， 无论你怎么按键都不会响应。



如果等待设置为0, 就意味着永久等待， 直到有任意一个按键按下。

```python
cv2.waitKey(0)
```



`waitKey` 返回的数值 是按下的按键字符，对应的ASCII编码。

```python
key_num = cv2.waitKey(0)
```



如果是等待有限时间例如， 

```python
key_num = cv2.waitKey(1000)
```

如果等待`1000ms` 也就是1s之后， 没有按键按下， 那么返回的这个值就是`-1`



我们在进行按键字符匹配的时候， 一般不会直接比对字符数值。 

你可以使用python的强制类型转换， 将数值转换为字符串`chr(value)` 



例如我们判断， 按键是否是k键的时候， 判断可以这么写:

```python
key_num = cv2.waitKey(0)

if chr(key_num) == 'k':
  print("k pressed...")
```

或者，你可以这么写

我们利用函数`ord(char)`， 可以将字符，转换为对应ASCII编码的数值。

```python
key_num = cv2.waitKey(0)

if key_num == ord('k'):
  print("k pressed...")
```



