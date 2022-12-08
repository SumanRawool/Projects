from django.contrib import admin
from courses.models import Course, Tag, Prerequisite, Learning, Video, Payment, UserCourse, CouponCode
from django.utils.html import format_html


# Register your models here.

class VideoAdmin(admin.TabularInline):
    model = Video


class TagAdmin(admin.TabularInline):
    model = Tag


class LearningAdmin(admin.TabularInline):
    model = Learning


class PrerequisteAdmin(admin.TabularInline):
    model = Prerequisite


class CourseAdmin(admin.ModelAdmin):
    inlines = [TagAdmin, LearningAdmin, PrerequisteAdmin, VideoAdmin]
    list_display = ["name", 'get_price', 'get_discount', 'active']
    list_filter = ("discount", "active")

    def get_discount(self, course):
        return f'{course.discount} %'

    def get_price(self, course):
        return f'₹ {course.price}'

    get_discount.short_description = "Discount"
    get_price.short_description = "Price"


class PaymentAdmin(admin.ModelAdmin):
    model = Payment
    list_display = ['order_id', 'get_user', 'get_course', 'status']
    list_filter = ['status', 'course']

    def get_user(self, payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")

    def get_course(self, payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class UserCourseAdminModel(admin.ModelAdmin):
    model = UserCourse
    list_display = ['click', 'get_user', 'get_course']
    list_filter = ['course']

    def get_user(self, UserCourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{UserCourse.user.id}'>{UserCourse.user}</a>")

    def click(self, UserCourse):
        return "Click to Open"

    def get_course(self, UserCourse):
        return format_html(
            f"<a target='_blank' href='/admin/courses/course/{UserCourse.course.id}'>{UserCourse.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"


class CouponCodeAdmin(admin.ModelAdmin):
    model = CouponCode


admin.site.register(Course, CourseAdmin)
admin.site.register(Video, )
admin.site.register(Payment, PaymentAdmin)
admin.site.register(UserCourse, UserCourseAdminModel)
admin.site.register(CouponCode,CouponCodeAdmin)
