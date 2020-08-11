from django.db import models

# Create your models here.


class SG_CON_PLANT_B(models.Model):
    """
    基础信息表
    """
    UID = models.CharField(max_length=64, null=False)
    NAME = models.CharField(max_length=128, unique=True, verbose_name='场站名称')
    REGION = models.ForeignKey("SG_DIC_REGION", to_field="CODE", on_delete=models.CASCADE, verbose_name='电场所属区域')
    PLANT_TYPE = models.ForeignKey("SG_DIC_PLANTSTATIONTYPE", to_field="CODE", on_delete=models.CASCADE, verbose_name='发电类型')
    MAX_VOLTAGE_TYPE = models.ForeignKey("SG_DIC_VOLTAGETYPE", to_field="CODE", on_delete=models.CASCADE, verbose_name='并网电压等级')
    VIRTUAL = models.BooleanField(default=False, verbose_name='是否虚拟电厂')
    class Meta:
        db_table = 'sg_con_plant_b'  # 在数据库中的表名，否则Django自动生成为app名字_类名
        verbose_name_plural = "场站基础信息表"

    def __str__(self):
        return self.NAME

class SG_DIC_VOLTAGETYPE(models.Model):
    """
    电压等级表
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True, verbose_name='电压等级id')
    NAME = models.CharField(max_length=64, verbose_name='电压等级名称')
    class Meta:
        db_table = 'sg_dic_voltagetype'
        verbose_name_plural = "电压等级表"


class SG_DIC_PLANTSTATIONTYPE(models.Model):
    """
    电场类型
    "CODE", "NAME", "EFFECT_FLAG"
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True, verbose_name='发电类型id')
    NAME = models.CharField(max_length=64, verbose_name='发电类型名称')
    EFFECT_FLAG = models.CharField(choices=(("Y", "可用"), ("N", "弃用")), max_length=1, verbose_name='是否有效')
    class Meta:
        db_table = 'sg_dic_plantstationtype'
        verbose_name_plural = "发电类型表"

class SG_DIC_REGION(models.Model):
    """
    电场类型
    "CODE", "NAME", "EFFECT_FLAG"
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True, verbose_name='区域id')
    NAME = models.CharField(max_length=64, verbose_name='区域名称')
    EFFECT_FLAG = models.CharField(choices=(("Y", "可用"), ("N", "弃用")), max_length=1, verbose_name='是否有效')
    class Meta:
        db_table = 'sg_dic_region'
        verbose_name_plural = "区域表"
