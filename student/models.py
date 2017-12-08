from django.db import models

# Create your models here.


#学院
class CollegeInfo(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField('学院名称',max_length=255)

#班级
class ClassInfo(models.Model):
    class_id = models.AutoField(primary_key=True)
    collect = models.ForeignKey(CollegeInfo, related_name='college_class')

    class_name = models.CharField('班级名称',max_length=255)
#学生
class StudentInfo(models.Model):
    stu_id = models.CharField('学号',max_length=20,primary_key=True)
    stu_class = models.ForeignKey(ClassInfo, related_name='class_stu')
    stu_name = models.CharField('姓名',max_length=100)
    stu_no = models.CharField('身份证',max_length=50)
    stu_img = models.CharField('照片路径',max_length=255)
    createTime = models.DateTimeField('注册时间')
