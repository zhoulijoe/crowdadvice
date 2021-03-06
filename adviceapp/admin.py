from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from adviceapp.models import UserProfile, Education, Industry, CareerField, \
                                CategoryCorrelation,MenteeProfile, MentorProfile, WorkExperience
                             #Skill, CareerGoal, AdviceType, Link,\
                             #MentoringLink, Tag, \
                             #Strength, Weakness, Honor, CaseRequest,\
                             #Advice, Comment


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 1


class UserProfileInline(admin.StackedInline):
    model = UserProfile


#class MenteeProfileInline(admin.StackedInline):
#    model = MenteeProfile


#class MentorProfileInline(admin.StackedInline):
#    model = MentorProfile


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [EducationInline, WorkExperienceInline]


#class SkillInline(admin.StackedInline):
#    model = Skill
#    extra = 1


#class LinkInline(admin.StackedInline):
#    model = Link
#    extra = 1


#class CareerGoalInline(admin.StackedInline):
#    model = CareerGoal
#    extra = 1


#class StrengthInline(admin.StackedInline):
#    model = Strength
#    extra = 1


#class WeaknessInline(admin.StackedInline):
#    model = Weakness
#    extra = 1


#class HonorInline(admin.StackedInline):
#    model = Honor
#    extra = 1


#class MenteeProfileAdmin(admin.ModelAdmin):
#    inlines = [MenteeProfileInline]#, SkillInline,
#               LinkInline, StrengthInline, WeaknessInline]


#class MentorProfileAdmin(admin.ModelAdmin):
#    inlines = [MentorProfileInline]#, SkillInline]


#class MentoringLinkAdmin(admin.ModelAdmin):
#    list_display = ('id', 'case', 'mentee', 'mentor', 'status', 'matching_score')


#class CaseRequestAdmin(admin.ModelAdmin):
#    list_display = ('id', 'mentee', 'date_created', 'title')


#class CategoryCorrelationAdmin(admin.ModelAdmin):
#    list_display = ('id', 'category1', 'category2', 'score')


#class AdviceAdmin(admin.ModelAdmin):
#    list_display = ('id', 'author', 'type', 'date_created')


#class CommentAdmin(admin.ModelAdmin):
#    list_display = ('id', 'author', 'advice', 'comment', 'date_created')


# Re-register UserAdmin
#admin.site.unregister(User)
#admin.site.register(User, UserAdmin)

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Industry)
admin.site.register(CareerField)
#admin.site.register(CategoryCorrelation, CategoryCorrelationAdmin)
#admin.site.register(Tag)
#admin.site.register(AdviceType)

#admin.site.register(MenteeProfile, MenteeProfileAdmin)
admin.site.register(MenteeProfile)
#admin.site.register(MentorProfile, MentorProfileAdmin)
admin.site.register(MentorProfile)

#admin.site.register(CaseRequest, CaseRequestAdmin)

#admin.site.register(MentoringLink, MentoringLinkAdmin)

#admin.site.register(Advice, AdviceAdmin)
#admin.site.register(Comment, CommentAdmin)