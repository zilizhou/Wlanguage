# -*- coding:utf-8 -*-
import re
varDict={}
keyWords_link=['+','+=','-','-=','>>',':-','&','@','*']#连接符关键词
keyWords_mon=['概念','实例','关系','属性','方法 ','规则','空','全部','同义']#单个的关键词
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
    if type(term)==list: #如果是一个list，则一个一个地查询
        pass  #这里面需要查询是否库中存储该信息的函数
    else:  #如果不是一个list，则单个查询
        pass  #这里面需要查询是否库中存储该信息的函数

    #这里调用查询是否有id的函数 返回这些id的所有信息（以字典的数据类型）放到list里面
    #['张三',[{},{}]]

    return infos



def infoConfirm(info):#这个函数收到的参数是由这部分组成，需要调用的函数名，和这个函数所需要的参数，并且是已经确定好的信息，
    #info的组成是[['function name','','']['如果是value，那么后面是具体的id或术语，如果是'query' 则是一个查询函数，需要将这个查询函数值做为第一个list的要加入的值']]
    tempList=[]
    if info[1][0]=='value':
        for i in range(1,len(info[1])):
            tempList.append(info[1][i])
        pass


    pass

def queryForFront(str):
    infos = []  # 返回前面的数据
    linfos = []
    rinfos = []
    dotFlag = str[0]  # 获取右侧是否有 '.'
    act = str[1]  # 获取操作符 += -= >> :-  + - = *
    left = str[2]  # 获取左侧表达式
    right = str[3]  # 获取右侧表达式
    if ',' not in right:#简单查询
        #调用简单查询函数，并将返回值组织成前台需要的格式
        pass
    else:#复杂查询
        # 调用复杂查询函数，并将返回值组织成前台需要的格式
        pass



def clauseInterpret(strcut): #根据对数据操作的几种类型，判断语句中属于哪几种类型。

    strLeft=strcut[1][0] #对连接符切分后的前半部分
    strRight=strcut[1][1]#对于连接符切分后的右半部分
    if (strcut[0]==''):#如果为空，说明是查询，因此要对查询字符串进行处理，这里因为是以逗号分开，所以直接用‘，’分开
        strRightCut = strRight.split(',')
        dotFlag='query'
    else: #如果不为空，则是有连接符的。这里要区分有点的，还没有点的表示
        if '.' in strRight:
            dotFlag='rdot'
            strRightCut = strRight.split(',')
        else:
            dotFlag='nrdot'
            if getInfoBracket('[]', strRight):
                strRightCut = ' '.join(getInfoBracket('[]', strRight)[0].split() ).split(' ') #
            else:
                strRightCut=strRight
    print(dotFlag,'---',strcut[0] ,'-----', strLeft, '--', strRightCut)
    return dotFlag, strcut[0], strLeft, strRightCut

def questionForFront(str):
    infos=[]#返回前面的数据
    linfos=[]
    rinfos=[]
    dotFlag=str[0] #获取右侧是否有 '.'
    act=str[1]#获取操作符 += -= >> :-  + - = *
    left=str[2]#获取左侧表达式
    right=str[3]#获取右侧表达式
    if act=='=':
        varDict[str[2]]=str[3]
    if act=='+=':
        if '.' not in left:  #这里是针对 概念+=[] 或 概念+=变量
            if left=='概念':
                linfos.append('增加概念函数名')
            if left=='实例':
                linfos.append('增加实例函数名')
            if left=='关系':
                linfos.append('增加关系函数名')
            if left=='属性':
                linfos.append('增加属性函数名')
            if '&' in right:
                right = varDict[right]  # 则把变量的值给right
            idInfos=termToId(right)#返回的格式为[学生，[001 dict][002 dict]]
            rinfos.append('nofunc')
            rinfos.append(idInfos)
        else:
            leftCut=left.split('.')
            linfos.append('添加关系，属性值的函数')
            for item in leftCut:
                idInfos=termToId(item)
                linfos.append(idInfos)
            if dotFlag=='nrdot':
                if '&' in right:
                    right = varDict[right]  # 则把变量的值给right
                idInfos = termToId(right)  # 返回的格式为[学生，[001 dict][002 dict]]
                rinfos.append('nofunc')
                rinfos.append(idInfos)
            if dotFlag=='rdot':
                rinfos.append('query')
                rightCut=right.split('.')
                for item in rightCut:
                    idInfos=termToId(item)
                    rinfos.append(idInfos)
    if act == '-=':
        if '.' not in left:  # 这里是针对 概念+=[] 或 概念+=变量
            if left == '概念':
                linfos.append('删除概念函数名')
            if left == '实例':
                linfos.append('删除实例函数名')
            if left == '关系':
                linfos.append('删除关系函数名')
            if left == '属性':
                linfos.append('删除属性函数名')
            if '&' in right:
                right = varDict[right]  # 则把变量的值给right
            idInfos = termToId(right)  # 返回的格式为[学生，[001 dict][002 dict]]
            rinfos.append('nofunc')
            rinfos.append(idInfos)
        else:
            leftCut = left.split('.')
            linfos.append('删除关系，属性值的函数')
            for item in leftCut:
                idInfos = termToId(item)
                linfos.append(idInfos)
            if dotFlag == 'nrdot':
                if '&' in right:
                    right = varDict[right]  # 则把变量的值给right
                idInfos = termToId(right)  # 返回的格式为[学生，[001 dict][002 dict]]
                rinfos.append('nofunc')
                rinfos.append(idInfos)
            if dotFlag == 'rdot':
                rinfos.append('query')
                rightCut = right.split('.')
                for item in rightCut:
                    idInfos = termToId(item)
                    rinfos.append(idInfos)
    if act=='>>':
        linfos.append('修改术语名的函数') #这里的四大关键词都有特殊的ID号
        leftCut=left.split('.')
        idInfos=termToId(leftCut[1])
        linfos.append(idInfos)
        rightCut=right.split('.')
        for item in rightCut:
            idInfos=termToId(item)
            linfos.append(idInfos)
    infos.append(linfos)
    infos.append(rinfos)
    return infos

        #     if leftCut[0]=='概念':
        #         linfos.append('更改术语的名称或类型函数')
        #         idInfos=termToId(leftCut[1])
        #         linfos.append(idInfos)
        #     if leftCut[0]=='实例':
        #         linfos.append('更改术语的名称或类型函数')
        #         idInfos=termToId(leftCut[1])
        #         linfos.append(idInfos)
        #     if leftCut[0]=='':
        #         linfos.append('更改术语的名称或类型函数')
        #         idInfos=termToId(leftCut[1])
        #         linfos.append(idInfos)
        #     if leftCut[0]=='概念':
        #         linfos.append('更改术语的名称或类型函数')
        #         idInfos=termToId(leftCut[1])
        #         linfos.append(idInfos)









    pass
    # infos=[]
    # act = str[1]
    # dotFlag=str[0]
    # left=str[2]
    # right=str[3]
    # if not dotFlag:
    #     if act=='=':
    #         varDict[str[2]]=str[3]
    #     if act=='+=':
    #         if left in keyWords_mon:#如果是四大关键词，则调用增加函数，注意要返回是否库里面有已有的信息。
    #
    #             if '&' in right: #如果是个变量
    #                 right=varDict[right]#则把变量的值给right
    #             infos=termToId(right)
    #
    #         else:
    #             pass
    #
    # return infos

    # if act:
    #     left = str[1].split('.')
    #     if ('.' in str[2][0]):
    #         right = str[2][0].split('.')
    #     else:
    #         right = str[2][0]
    # else:
    #     left=''
    #     right = str[2]
    #     for tri in right:
    #         temp=tri.split('.')
    #         print(temp)


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
    str1 = clauseUtoS('bb.aa+=[学生 课程]')
    # str1 = clauseUtoS('张三.同学+=[李四 王五].[朋友 同学]')
    # str1=clauseUtoS('概念+=[学生       同学]')
    # str1 = clauseUtoS('&学生们=李四')
    # str1=clauseUtoS('&学生们=[李四 王五]')
    # str1 = clauseUtoS('&朋友们=张三.朋友')
    # str1=clauseUtoS('概念+=学生们')

    # str1 = clauseUtoS('&学生们=张三.同学')
    str2=oneClauseCut(str1)

    str3=clauseInterpret(str2)
    str4=questionForFront(str3)

    # print(str2[0].split('.'))