from django.db import models

# Create your models here.


class SG_CON_PLANT_B(models.Model):
    """
    基础信息表
    """
    UID = models.CharField(max_length=64, null=False)
    NAME = models.CharField(max_length=128, unique=True)
    REGION = models.ForeignKey("SG_DIC_REGION", to_field="CODE", on_delete=models.CASCADE)
    PLANT_TYPE = models.ForeignKey("SG_DIC_PLANTSTATIONTYPE", to_field="CODE", on_delete=models.CASCADE)
    MAX_VOLTAGE_TYPE = models.ForeignKey("SG_DIC_VOLTAGETYPE", to_field="CODE", on_delete=models.CASCADE)
    VIRTUAL = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "场站基础信息表"

    def __str__(self):
        return self.NAME

class SG_DIC_VOLTAGETYPE(models.Model):
    """
    电压等级表
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True)
    NAME = models.CharField(max_length=64)
    class Meta:
        verbose_name_plural = "场站基础信息表"


class SG_DIC_PLANTSTATIONTYPE(models.Model):
    """
    电场类型
    "CODE", "NAME", "EFFECT_FLAG"
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True)
    NAME = models.CharField(max_length=64)
    EFFECT_FLAG = models.CharField(choices=(("Y", "可用"), ("N", "弃用")), max_length=1)
    class Meta:
        verbose_name_plural = "场站基础信息表"

class SG_DIC_REGION(models.Model):
    """
    电场类型
    "CODE", "NAME", "EFFECT_FLAG"
    """
    CODE = models.IntegerField(null=False, db_index=True, unique=True)
    NAME = models.CharField(max_length=64)
    EFFECT_FLAG = models.CharField(choices=(("Y", "可用"), ("N", "弃用")), max_length=1)
    class Meta:
        verbose_name_plural = "场站基础信息表"
