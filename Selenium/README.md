# Why Selenium?
Some websites don't like to be scrapped and in that case you need to **disguise your webscraping bot as a Human Being**

# What is locator or css selector or xpath?

Locator can be termed as an address that identifies a web element uniquely within the webpage. Locators are the HTML properties of a web element which tells the Selenium about the web element it need to perform action on.

There is a diverse range of web elements. 

Types of Locators in Selenium

![687474703a2f2f63646e322e736f66747761726574657374696e6768656c702e636f6d2f77702d636f6e74656e742f71612f75706c6f6164732f323031342f31302f54797065732d6f662d4c6f6361746f72732d696e2d53656c656e69756d2d312e6a7067](https://user-images.githubusercontent.com/36659683/44990077-8c215d80-afad-11e8-8703-f0f1f5d7ab3d.jpg)

The most common amongst them are:
* Xpath
* CSS - Selector
* Tag Name

## XPATH

Xpath is used to locate a web element based on its XML path. XML stands for Extensible Markup Language and is used to store, organize and transport arbitrary data. It stores data in a key-value pair which is very much similar to HTML tags. Both being mark up languages and since they fall under the same umbrella, xpath can be used to locate HTML elements.

The fundamental behind locating elements using Xpath is the traversing between various elements across the entire page and thus enabling a user to find an element with the reference of another element.

## CSS-Selector

CSS Selector is combination of an element selector and a selector value which identifies the web element within a web page. The composite of element selector and selector value is known as Selector Pattern.

## Tag Name Locator:

Tag Name locator is used to find the elements matching the specified Tag Name. It is very helpful when we want to extract the content within a Tag.

#### DEMO
![findelement-and-findelements-demo](https://user-images.githubusercontent.com/36659683/44990638-436aa400-afaf-11e8-960b-8a4f92cb4841.gif)

## Reference:
Selenium Documentation - https://www.seleniumhq.org/docs/
Basic Selenium Usage - https://www.youtube.com/watch?v=bhYulVzYRng
