import maya.cmds as cmds

#Decimal to Alphabet Converter
def decimalToAlphabet(x):
    char='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if x<0:
        return None

    result=''

    while x>0:
        result=char[x%26-1]+result
        x=x/26

    return result

# Refresh
def refresh():
    # Prefix
    if cmds.checkBox('cbPF',q=True, v=True):
        if cmds.checkBox('cbUS',q=True, v=True):
            pf='[Prefix]_'
        else:
            pf='[Prefix]'
    else:
        pf=''
    # Suffix
    if cmds.checkBox('cbSF',q=True, v=True):
        if cmds.checkBox('cbUS',q=True, v=True):
            sf='_[Suffix]'
        else:
            sf='[Suffix]'
    else:
        sf=''
    # Name Override Check
    name = ''
    if cmds.checkBox('cbON', q=True, v=True):
        name = '[Override Name]'
    else:
        name = '[Original Name]'

    rp = pf + name + sf
    cmds.text('textPP', e=True, l='Rename Preview : '+rp)

# Rename
def rename():
    obj = cmds.ls(sl=True)
    objLen = len(obj)


    # Rename Process
    for i in range(objLen):
        s=''

        if cmds.checkBox('cbPF',q=True, v=True):
            if cmds.radioButtonGrp('rbPF', q=True, sl=True)==1:
                s=s+decimalToAlphabet(i+1)
            if cmds.radioButtonGrp('rbPF', q=True, sl=True)==2:
                s=s+cmds.textField('tfPF', q=True, tx=True)

            if cmds.checkBox('cbUS', q=True, v=True):
                s=s+'_'

        if cmds.checkBox('cbON',q=True, v=True):
            s=s+cmds.textField('tfON', q=True, tx=True)
        else:
            s=s+obj[i]

        if cmds.checkBox('cbSF',q=True, v=True):
            if cmds.checkBox('cbUS', q=True, v=True):
                s=s+'_'

            if cmds.radioButtonGrp('rbSF', q=True, sl=True)==1:
                s=s+decimalToAlphabet(i+1)
            if cmds.radioButtonGrp('rbSF', q=True, sl=True)==2:
                s=s+str(i+1)
            if cmds.radioButtonGrp('rbSF', q=True, sl=True)==3:
                s=s+cmds.textField('tfSF', q=True, tx=True)

        cmds.rename(obj[i],s)
        #print(s)
    #print()

aCode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nCode = '123456789'
w = 500
h = 400
# pf : Prefix, sf : Suffix
pf='[Prefix]'
sf='[Suffix]'
# us : Underscore
us = ''
# rp : Rename Preview
rp = ''
# on : Override Name
on = ''

# Window Process
def main():
    win = cmds.window(t='miyamoRenamer', widthHeight=(w,h))
    colum = cmds.columnLayout(adj=True, rs=10, cal='center')
    # Prefix
    cmds.checkBox('cbPF', l='Prefix',v=False, onc='cmds.rowLayout("rlPF", e=True, en=True)', ofc='cmds.rowLayout("rlPF", e=True, en=False)')
    cmds.rowLayout('rlPF', nc=2, en=False)
    cmds.radioButtonGrp('rbPF', w=300, ct2=('left','left'), nrb=2,  la2=('Alphabet','Custom'),sl=1, on2='cmds.textField("tfPF", e=True, en=True)', of2='cmds.textField("tfPF", e=True, en=False)')
    cmds.textField('tfPF', en=False)
    cmds.setParent('..')
    # Suffix
    cmds.checkBox('cbSF', l='Suffix', v=False, onc='cmds.rowLayout("rlSF", e=True, en=True)', ofc='cmds.rowLayout("rlSF", e=True, en=False)')
    cmds.rowLayout('rlSF', nc=2, en=False)
    cmds.radioButtonGrp('rbSF', w=300, ad3=1, cw3=(90,90,90),ct3=('left','left','left'), nrb=3,  la3=('Alphabet','Number','Custom'),sl=1, on3='cmds.textField("tfSF", e=True, en=True)', of3='cmds.textField("tfSF", e=True, en=False)')
    cmds.textField('tfSF', en=False)
    cmds.setParent('..')

    # Separator
    cmds.separator()

    # Override Name
    cmds.checkBox('cbON', l='Override Name', v=False, onc='cmds.textField("tfON", e=True, en=True)', ofc='cmds.textField("tfON", e=True, en=False)')
    cmds.textField('tfON', w=200, en=False)

    # Separator
    cmds.separator()

    # Attach _
    cmds.checkBox('cbUS', l='Attach _', v=True)

    # Separator
    cmds.separator()

    cmds.button(l='Preview', c='refresh()')
    cmds.text('textPP', l='Rename Preview : ' + rp, al='left')
    cmds.button(l='Rename', h=40, c='rename()')

    cmds.showWindow()

main()
