from django.db import models


# Create your models here.
class GoodsType:
    goods_name = models.CharField(max_length=20, verbose_name='种类名称')
    goods_logo = models.CharField(max_length=20, verbose_name='标识')
    image = models.ImageField(upload_to='type', verbose_name='商品类型图片')

    class Meta:
        db_table = 'df_goods_type'
        verbose_name = '商品种类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods_name
