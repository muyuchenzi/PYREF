import os
from PIL import Image,ImageDraw,ImageFont

'''

#NOTE作为一个参考，不做具体分析，只是一个图片处理模块的使用案例而已
'''
def get_position(image_width,image_height,text_width,text_height,position_id=9,margin=0):
    '''
    获取文字位置，position_id
    1: 左上, 2: 中上, 3: 右上
    4: 中左, 5: 正中, 6: 中右
    7: 左下, 8: 下中, 9: 右下
    :param image_width: 图片宽度
    :param image_height: 图片高度
    :param text_width: 文字宽度
    :param text_height: 文字高度
    :param position_id: 位置ID，1-9，默认是9（右下）
    :param margin: 边距值，默认为10px
    :return: 文字位置的(x, y)元组
    '''

    margin = 10
    if position_id == 1:
        return (margin, margin)
    elif position_id == 2:
        return (image_width // 2 - text_width // 2, margin)
    elif position_id == 3:
        return (image_width - text_width - margin, margin)
    elif position_id == 4:
        return (margin, image_height // 2 - text_height // 2)
    elif position_id == 5:
        return (image_width // 2 - text_width // 2, image_height // 2 - text_height // 2)
    elif position_id == 6:
        return (image_width - text_width - margin, image_height // 2 - text_height // 2)
    elif position_id == 7:
        return (margin, image_height - text_height - margin)
    elif position_id == 8:
        return (image_width // 2 - text_width // 2, image_height - text_height - margin)
    elif position_id == 9:
        return (image_width - text_width - margin, image_height - text_height - margin)

def add_watermark(filename,text,font_name='Roboto-Italic.ttf',font_size=20,font_opacity=50,
                    position_id=9):
    '''
    增加水印
    :param filename: 要加水印的文件(dir/file.png)
    :param text: 水印文字
    :param font_name: 默认为Roboto-Italic.ttf字体
                      你也可以使用自己的字体，确保代码能够找到这个字体文件（在当前目录或者系统字体目录中）
    :param font_size: 字体大小，默认值为20px
    :param font_opacity: 透明度，默认为50%
    :param position_id: 位置ID，1-9，默认是9（右下）
    :return: 
    '''

    with Image.open(filename).convert("RGBA") as base:
        # 创建一个新的透明画面，大小和原图片一样
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        # 使用指定的字体
        fnt = ImageFont.truetype(font_name, font_size)
        # 准备“画”文字
        d = ImageDraw.Draw(txt)
        # 得到文字的宽度和高度
        text_width, text_height = d.textsize(text, font=fnt)
        # 得到文字的位置
        pos = get_position(base.size[0], base.size[1], text_width, text_height, position_id=position_id)
        # 将文字“画”到画布上
        d.text(pos, text, font=fnt, fill=(255, 255, 255, 256 * font_opacity // 100))
        # 将画布和原图片合并
        out = Image.alpha_composite(base, txt)

        # 保存图片文件
        out_filename = 'watermark/{}'.format(os.path.basename(filename))
        if not os.path.exists('watermark'):
            os.makedirs('watermark')
        out.save(out_filename, 'PNG')

if __name__=="__main__":
    text = input('请输入水印文字: ').strip()
    font_size = int(input('请输入文字大小: [20]') or '20')
    font_opacity = int(input('请输入文字透明度: [50]') or '50')
    # 1: 左上, 2: 中上, 3: 右上
    # 4: 中左, 5: 正中, 6: 中右
    # 7: 左下, 8: 下中, 9: 右下
    position_id = int(input('请输入水印位置: [9]') or '9')

    for f in os.listdir('images'):
        if f.endswith('.png'):
            filename = 'images/{}'.format(f)
            print('给{}增加水印'.format(filename))
            add_watermark(filename=filename, text=text, font_size=font_size, font_opacity=font_opacity,
                          position_id=position_id)
