from django.db import models

# Create your models here.
#学院
class CollegeInfo(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField('学院名称',max_length=255,null=True)

#班级
class ClassInfo(models.Model):
    class_id = models.AutoField(primary_key=True)
    collect = models.ForeignKey(CollegeInfo, related_name='college_class')
    class_name = models.CharField('班级名称',max_length=255,null=True)

#照片集
class Image_Collect(models.Model):
    image_id = models.AutoField(primary_key=True)
    stu_class = models.ForeignKey(ClassInfo, related_name='class_image',blank=True)
    image_src = models.CharField("照片地址",max_length=255,null=True)
    image_title = models.CharField("照片标题",max_length=255,null=True)
    createTime = models.DateTimeField('拍摄时间',null=True)
    creator = models.CharField("上传人",max_length=255,null=True)

#学生
class StudentInfo(models.Model):
    stu_id = models.CharField('学号',max_length=20,primary_key=True,blank=False)
    stu_class = models.ForeignKey(ClassInfo, related_name='class_stu',blank=True)
    stu_name = models.CharField('姓名',max_length=100,null=True)
    stu_cnname = models.CharField("姓名拼音",max_length=255,null=True)
    stu_no = models.CharField('身份证',max_length=50,null=True)
    stu_img = models.CharField('照片路径',max_length=255,null=True)
    stu_bir = models.DateField("生日",null=True)
    stu_sex = models.CharField('性别', max_length=10, null=True)
    stu_phone = models.CharField("手机号",max_length=100,null=True)
    stu_qq = models.CharField("QQ号",max_length=100,null=True)
    stu_wechat = models.CharField("微信", max_length=100,null=True)
    stu_home = models.CharField("现居地",max_length=255,null=True)
    stu_desc = models.CharField("个人简介",max_length=255,null=True)
    stu_password = models.CharField("登陆密码",max_length=255,null=True)
    stu_about = models.CharField("班级感言",max_length=255,null=True)
    createTime = models.DateTimeField('注册时间',null=True)
    stuTime = models.DateTimeField('入学时间', null=True)
