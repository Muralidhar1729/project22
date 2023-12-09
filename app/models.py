from django.db import models

class dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100,null=False)
    loc=models.CharField(max_length=100)

class emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100,)
    sal=models.IntegerField()
    comm=models.IntegerField()
    dname=models.CharField(max_length=100,)
    hiredate=models.DateField()
    deptno=models.ForeignKey(dept,on_delete=models.CASCADE)
    mgr=models.CharField(max_length=100,)

class bonus(models.Model):
    sal=models.IntegerField(primary_key=True)
    ename=models.ForeignKey(emp,on_delete=models.CASCADE)
    comm=models.CharField(max_length=100,null=True)
    job=models.CharField(max_length=100,null=False)

class salgrade(models.Model):
    hisal=models.IntegerField(primary_key=True)
    losal=models.CharField(max_length=100)
    grade=models.CharField(max_length=100)





    



