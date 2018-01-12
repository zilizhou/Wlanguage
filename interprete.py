# -*- coding:utf-8 -*-
import re

keyWords_link=['+','+=','-','-=','>>',':-','&','@','*']#连接符关键词
keyWords_mon=['概念','实例','关系','属性','空','全部','同义']#单个的关键词
#知识库中默认有 is_a has_subclass has_instance instance_of 或者用中文，是  有子类 有实例 是实例
#对每一条语句进行解析，这里分成多种情况，即含有连接符关键词的一些语句，根据连接符关键词来对语句进行判断。
def getInfoBracket(symbol,str):#对于有中括号和小括号的语句，提取其中的内容。在分词后再来提取内容。
    pattern1 = r'\((.+)\)'#查询（）中的内容
    pattern2 = r'\[(.*?)\]'#查询[]中的内容
    # pattern3 = r'\@(.+)\='#获取@与（间的内容，其实就是获取方法。
    #pattern4 = r'\@(.+)\('
    if (symbol=='()'):
        info=re.findall(pattern1,str)
    if (symbol=='[]'):
        info=re.findall(pattern2,str)

    return info

#对数据操作的几种类型：
# 1. 对具体的概念进行增删改，语句如下：概念+＝学生
#                                     实例+＝张三
#                                     关系+＝同学
#                                     属性+＝学号
#                                      
#                                     概念-=学生
#                                     实例-=张三
#                                     关系-＝同学
#                                     属性－＝学号
#
#                                     概念.学生>>student
#                                     实例.张三>>张小明

def termToId(term):
    infos=[]
    #这里调用查询是否有id的函数 返回这些id的所有信息（以字典的数据类型）放到list里面


    return infos



def idConfirm(info):



    pass



def clauseInterpret(strcut): #根据对数据操作的几种类型，判断语句中属于哪几种类型。
    print(strcut)
    strLeft=strcut[1][0] #对连接符切分后的前半部分以'.'分割
    strTemp=strcut[1][1]
    print(strcut[0])

    if (strcut[0]==''):
        strRightCut = strTemp.split(',')
    else:
        if getInfoBracket('[]', strTemp):
            strRightCut = getInfoBracket('[]', strTemp)[0].split(' ')  #
        else:
            strRightCut = strTemp.split(',')

    print(strcut[0], '-----', strLeft, '--', strRightCut)
    return strcut[0], strLeft, strRightCut

def questionForFront(str):
    act = str[0]
    if act:
        left = str[1].split('.')
        right = str[2][0].split('.')
    else:
        left=''
        right = str[2]
        for



    print(act, '$$', left, '$$', right)

    pass

    # if (strLeft[0] in keyWords_mon):#看一下这一项中的内容是否是关键词中的一员，如果是，则执行概念、实例、关系和属性的增加和删除
    #     if (strcut[0]=='+='):
    #         if (strLeft[0]=='概念'):#增加概念，具体概念是strRight
    #             print(strcut[0],strLeft)
    #             pass
    #         if (strLeft[0]=='实例'):#增加实例，具体实例是strRight
    #             print(strcut[0] , strLeft)
    #             pass
    #         if (strLeft[0]=='关系'):#增加关系，具体关系是strRight
    #             print(strcut[0] , strLeft)
    #             pass
    #         if (strLeft[0]=='属性'):#增加属性，具体属性是strRight
    #             print(strcut[0] , strLeft)
    #             pass
    #     if (strcut[0] == '-='):
    #         if (strLeft[0] == '概念'):#删除概念，具体概念是strRight
    #             pass
    #         if (strLeft[0] == '实例'):#删除实例，具体实例是strRight
    #             pass
    #         if (strLeft[0] == '关系'):#删除关系，具体关系是strRight
    #             pass
    #         if (strLeft[0] == '属性'):#删除属性，具体属性是strRight
    #             pass
    #     if (len(strLeft)>1):
    #         if (strLeft[0] == '概念'):#修改概念术语，具体概念是strRight
    #             pass
    #         if (strLeft[0] == '实例'):#修改实例术语，具体实例是strRight
    #             pass
    #         if (strLeft[0] == '关系'):#修改关系术语，具体关系是strRight
    #             pass
    #         if (strLeft[0] == '属性'):#修改属性术语，具体属性是strRight
    #             pass
    # else: #如果前半部分包含多项,并且没有概念，实例，关系和属性，也就是具体的概念的情况下 进行的操作
    #     if (strcut[0] == '-='):
    #
    #         pass






def oneClauseCut(str):
    if '+' in str:
        if '+=' in str:#涉及到知识编辑 增加
            strcut=str.split('+=')
            symbol='+='

        else:  #涉及到知识计算  - 的情况
            strcut = str.split('+')
            symbol = '+'

    if '-' in str:
        if '-=' in str: #涉及到知识编辑 减少
            strcut = str.split('-=')
            symbol = '-='
        else:  #涉及到知识计算  - 的情况
            strcut = str.split('-')
            symbol = '-'

    if '>>' in str: #用于术语的编辑
        strcut = str.split('>>')
        symbol = '>>'

    if ':-' in str: #涉及到规则的情况
        strcut = str.split(':-')
        symbol = ':-'

    if '*' in str:# 对于知识计算的情况
        strcut = str.split('*')
        symbol = '*'
    if ('=' in str) and ('+=' not in str) and ('-=' not in str):
        strcut = str.split('=') #对于只有=号的情况，就是涉及到了变量
        symbol = '='
    if ('=' not in str) and ('+=' not in str) and ('-=' not in str) and ('*' not in str) and (':-' not in str) and ('>>' not in str):
        strcut = ['']+[str] #对于查询的情况
        symbol = ''

    return (symbol,strcut)
def clauseUtoS(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # 全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # 全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring

if __name__ == '__main__':
    # s=getInfoBracket('[]', '[(@概念),学生]([+=学生,test]')
    # print(s[0].split(','))
    str1 = clauseUtoS('[张三 李四].同学.&A, &A.朋友.&B, &B.&D.李四,@大于（&A.年龄  30）')
    # str1=clauseUtoS('&A.老乡.&B:-&A.籍贯.&C,&B.籍贯.&C ')#&A.老乡.&B:-&A.籍贯.&C,&B.籍贯.&C  aa.bb+=[学生，同学]
    # str1 = clauseUtoS('aa.bb+=学生')
    # str1=clauseUtoS('概念+=学生')
    str2=oneClauseCut(str1)

    str3=clauseInterpret(str2)
    str4=questionForFront(str3)

    # print(str2[0].split('.'))