
from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
import operator


class CognitiveDistortion(models.Model):
    
    name = models.CharField(max_length=140)
    description = models.TextField(default="")

    def __unicode__(self):
        return self.name


#
# Burns Depression Checklist - BDC
# 

class BDC(models.Model):
    
    QUESTION_FIELDS = ('q_1', 'q_2', 'q_3', 'q_4', 'q_5',
                       'q_6', 'q_7', 'q_8', 'q_9', 'q_10',
                       'q_11', 'q_12', 'q_13', 'q_14', 'q_15',
                       'q_16', 'q_17', 'q_18', 'q_19', 'q_20',
                       'q_21', 'q_22', 'q_23', 'q_24', 'q_25',)

    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()

    def q(title, description):
        ANSWER_CHOICES = (
            (0, '0 - Not at all'),
            (1, '1 - Somewhat'),
            (2, '2 - Moderately'),
            (3, '3 - A lot'),
            (4, '4 - Extremely'),
        )
        return models.IntegerField(title, help_text=description, 
                                   max_length=1, default=0, choices=ANSWER_CHOICES)


    # Questions
    q_1  = q(_("Question 1"),  _("Feeling sad or down in the dumps"))
    q_2  = q(_("Question 2"),  _("Feeling unhappy or blue"))
    q_3  = q(_("Question 3"),  _("Crying spells or tearfullness"))
    q_4  = q(_("Question 4"),  _("Feeling discouraged"))
    q_5  = q(_("Question 5"),  _("Feeling hopeless"))
    q_6  = q(_("Question 6"),  _("Low self-esteem"))
    q_7  = q(_("Question 7"),  _("Feeling worthless or inadequate"))
    q_8  = q(_("Question 8"),  _("Guilt or shame"))
    q_9  = q(_("Question 9"),  _("Criticizing yourself or blaming yourself"))
    q_10 = q(_("Question 10"), _("Difficulty making decisions"))
    q_11 = q(_("Question 11"), _("Loss of interest in family, friends or colleagues"))
    q_12 = q(_("Question 12"), _("Loneliness"))
    q_13 = q(_("Question 13"), _("Spending less time with family or friends"))
    q_14 = q(_("Question 14"), _("Loss of motivation"))
    q_15 = q(_("Question 15"), _("Loss of interest in work or other activities"))
    q_16 = q(_("Question 16"), _("Avoiding work or other activities"))
    q_17 = q(_("Question 17"), _("Loss of pleasure or satisfaction in life"))
    q_18 = q(_("Question 18"), _("Feeling tired"))
    q_19 = q(_("Question 19"), _("Difficulty sleeping or sleeping too much"))
    q_20 = q(_("Question 20"), _("Decreased or increased appetite"))
    q_21 = q(_("Question 21"), _("Loss of interest in sex"))
    q_22 = q(_("Question 22"), _("Worrying about your health"))
    q_23 = q(_("Question 23"), _("Do you have any suicidal thoughts?"))
    q_24 = q(_("Question 24"), _("Would you like to end your life?"))
    q_25 = q(_("Question 25"), _("Do you have a plan for harming yourself?"))

    del q

    @property
    def questions(self):
        for key in self.QUESTION_FIELDS:
            yield (getattr(self, key), self._meta.get_field(key))

    @property
    def score(self):
        score = 0
        for q,f in self.questions:
            score += q

        return score


#
# Novaco anger scale - NAS
#

class NovacoAngerScale(models.Model):
    
    STATEMENT_FIELDS = ('s_1', 's_2', 's_3', 's_4', 's_5',
                       's_6', 's_7', 's_8', 's_9', 's_10',
                       's_11', 's_12', 's_13', 's_14', 's_15',
                       's_16', 's_17', 's_18', 's_19', 's_20',
                       's_21', 's_22', 's_23', 's_24', 's_25',)

    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()

    def s(title, description):
        ANSWER_CHOICES = (
            (0, '0 - Very little or no annoyance'),
            (1, '1 - A little irritated'),
            (2, '2 - Moderately upset'),
            (3, '3 - Quite angry'),
            (4, '4 - Very angry'),
        )
        return models.IntegerField(title, help_text=description, 
                                   max_length=1, default=0, choices=ANSWER_CHOICES)

    # Statements
    s_1  = s(_("Statement 1"),  _("You unpack an appliance you have just bought, plug it in and discover it doesn't work."))
    s_2  = s(_("Statement 2"),  _("Being overcharged by a repairman who has you over a barrel."))
    s_3  = s(_("Statement 3"),  _("Being singled out for correction, when the actions of others go unnoticed."))
    s_4  = s(_("Statement 4"),  _("Getting your car stuck in the mud or snow."))
    s_5  = s(_("Statement 5"),  _("You are talking to someone and they don't answer you."))
    s_6  = s(_("Statement 6"),  _("Someone pretends to be something they are not."))
    s_7  = s(_("Statement 7"),  _("When you are struggling to carry four cups of coffee to your table at a cafeteria, someone bumps into you, spilling the coffee."))
    s_8  = s(_("Statement 8"),  _("You have hung up your clothes, but someone knocks them down and fails to pick them up."))
    s_9  = s(_("Statement 9"),  _("You are hounded by a salesperson from the moment you walk into a store."))
    s_10 = s(_("Statement 10"), _("You have made arrangements to go somewhere with a person who backs off at the last minute and leaves you hanging."))
    s_11 = s(_("Statement 11"), _("Being joked about or teased."))
    s_12 = s(_("Statement 12"), _("You are stalled at a traffic light, and the guy behind you keeps blowing his horn."))
    s_13 = s(_("Statement 13"), _("You accidentally make the wrong kind of turn in a parking lot. As you get out of your car, someone yells, 'Where did you learn to drive?'."))
    s_14 = s(_("Statement 14"), _("Someone makes a mistake and blames it on you."))
    s_15 = s(_("Statement 15"), _("You are trying to concentrate, but a person near you is tapping their foot."))
    s_16 = s(_("Statement 16"), _("You lend someone an important book or tool, and they fail to return it."))
    s_17 = s(_("Statement 17"), _("You have had a busy day, and the person you live with starts to complain about how you forgot to do something that you agreed to do."))
    s_18 = s(_("Statement 18"), _("You are trying to discuss something important with your mate or partner who isn't giving you a chance to express your feelings."))
    s_19 = s(_("Statement 19"), _("You are in a discussion with someone who persists in arguing about a topic they know very little about."))
    s_20 = s(_("Statement 20"), _("Someone sticks his or her nose into an argument between you and someone else."))
    s_21 = s(_("Statement 21"), _("You need to get somewhere quickly, but the car in front of you is going 25 mph in a 40 mph zone, and you can't pass."))
    s_22 = s(_("Statement 22"), _("Stepping on a gob of chewing gum."))
    s_23 = s(_("Statement 23"), _("Being mocked by a small group of people as you pass them."))
    s_24 = s(_("Statement 24"), _("In a hurry to get somewhere, you tear a good pair of slacks on a sharp object."))
    s_25 = s(_("Statement 25"), _("You use your last dime to make a phone call, but you are disconnected before finishing dialing and the dime is lost."))

    del s

    @property
    def statements(self):
        for key in self.STATEMENT_FIELDS:
            yield (getattr(self, key), self._meta.get_field(key))

    @property
    def score(self):
        score = 0
        for s,f in self.statements:
            score += s

        return score


# 
# Two Column Sheet
# 

class TwoColumn(models.Model):
    
    user = models.ForeignKey(User)

    name = models.CharField(_("Sheet name"), max_length=140)

    column_one_title = models.CharField(_("Column one name"), max_length=140)
    column_two_title = models.CharField(_("Column two name"), max_length=140)

    
class TwoColumnEntry(models.Model):
    
    sheet = models.ForeignKey(TwoColumn, related_name='entries')
    timestamp = models.DateTimeField(auto_now_add=True)

    column_one = models.TextField(_("Column one"), default="", blank=True)
    column_two = models.TextField(_("Column two"), default="", blank=True)

# 
# Triple Column Technique - TCT
#

class TripleColumnEntryManager(models.Manager):
    
    def get_query_set(self):
        return TripleColumnQuerySet(self.model)

 
class TripleColumnQuerySet(QuerySet):

    def distortion_statistics(self):
        counts = {}
        for entry in self:
            for distortion in entry.cognitive_distortions.all():
                if not counts.has_key(distortion):
                    counts[distortion] = 0
                counts[distortion] = counts[distortion] + 1

        counts = sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)

        return counts


class TripleColumn(models.Model):
    
    user = models.ForeignKey(User)

    
class TripleColumnEntry(models.Model):
    
    triplecolumn = models.ForeignKey(TripleColumn, related_name='entries')
    timestamp = models.DateTimeField(auto_now_add=True)

    automatic_thought     = models.TextField(_("Automatic thought"), default="", blank=True)
    cognitive_distortions = models.ManyToManyField(CognitiveDistortion, 
                                                   verbose_name=_("Cognitive distortions"),
                                                   related_name="triplecolumn_entries")
    rational_response     = models.TextField(_("Rational Response"), default="", blank=True)
    
    objects = TripleColumnEntryManager()
    
# 
# Daily Activity Schedule
#

class DailyActivitySchedule(models.Model):
    
    user = models.ForeignKey(User)
    date = models.DateField()

    def create_entries(self):
        for entry in self.entries.all():
            entry.delete()

        for start,end in ((9,10), (10,11),(11,12),(12,13),(13,14),
                     (14,15),(15,16),(16,17),(17,18),(18,19),
                     (19,20),(20,21),(21,24),):
            entry = DailyActivityScheduleEntry(schedule=self, start=start,end=end)
            entry.save()

class DailyActivityScheduleEntry(models.Model):
    
    schedule = models.ForeignKey(DailyActivitySchedule, related_name='entries')

    start = models.IntegerField(max_length=2)
    end = models.IntegerField(max_length=2)

    prospective = models.TextField(_("Prospective"), default="", blank=True)
    retrospective = models.TextField(_("Retrospective"), default="", blank=True)

    @property
    def human_hour(self):
        return "%d - %d" % (self.start, self.end)


# 
# Anti Procrastination Sheet - APS
#

class AntiProcrastinationSheet(models.Model):
    
    user = models.ForeignKey(User)
    date = models.DateField(_("Day"))
    
class AntiProcrastinationSheetEntry(models.Model):
    
    sheet = models.ForeignKey(AntiProcrastinationSheet, related_name='entries')

    activity               = models.CharField(_("Activity"), default="", blank=True, max_length=256)

    predicted_difficulty   = models.IntegerField(_("Predicted difficulty"), max_length=3, default=0)
    predicted_satisfaction = models.IntegerField(_("Predicted satisfaction"), max_length=3, default=0)

    actual_difficulty      = models.IntegerField(_("Actual difficulty"), max_length=3, default=0)
    actual_satisfaction    = models.IntegerField(_("Actual satisfaction"), max_length=3, default=0)
    
    
