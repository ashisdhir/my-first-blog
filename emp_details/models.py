from django.db import models

# Create your models here.


class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)










#
#
# class Fruit(models.Model):
#     name = models.CharField(max_length=10, primary_key=True)
#
#
# class EmpData(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'SMALL'),
#         ('M', 'MEDIUM'),
#         ('L', 'LARGE'),
#     )
#     emp_id = models.IntegerField(default=0)
#     emp_name = models.CharField(max_length=20)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
#
#     def __str__(self):
#         return str(self.emp_id)
#
#
#
# class EmpDesc(models.Model):
#     empdata = models.ForeignKey(EmpData, on_delete=models.CASCADE)
#     emp_addr = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.emp_addr
#
#
# class Person(models.Model):
#     SHIRT_SIZES = (
#         ('S', 'Small'),
#         ('M', 'Medium'),
#         ('L', 'Large'),
#     )
#     name = models.CharField(max_length=60)
#     shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)