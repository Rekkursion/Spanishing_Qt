from enum import Enum

from enums.personal import Personal
from enums.tense import Tense
from utils.character_checker import CharChecker


# noinspection SpellCheckingInspection
class VerbType(Enum):
    # the ar-verb
    AR = {
        Tense.PARTICLES: {
            Personal.PRESENT_PARTICLE: ('-ar', '+ando'),
            Personal.PAST_PARTICLE: ('-ar', '+ado')
        },
        Tense.INDICATIVE_PRESENT: {
            Personal.YO: ('-ar', '+o'),
            Personal.TÚ: ('-ar', '+as'),
            Personal.ÉL__ELLA__USTED: ('-ar', '+a'),
            Personal.NOSOTROS: ('-ar', '+amos'),
            Personal.VOSOTROS: ('-ar', '+áis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ar', '+an')
        },
        Tense.INDICATIVE_PRETERITE: {
            Personal.YO: ('-ar', '+é'),
            Personal.TÚ: ('-ar', '+aste'),
            Personal.ÉL__ELLA__USTED: ('-ar', '+ó'),
            Personal.NOSOTROS: ('-ar', '+amos'),
            Personal.VOSOTROS: ('-ar', '+asteis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ar', '+aron')
        },
        Tense.INDICATIVE_IMPERFECT: {
            Personal.YO: ('-ar', '+aba'),
            Personal.TÚ: ('-ar', '+abas'),
            Personal.ÉL__ELLA__USTED: ('-ar', '+aba'),
            Personal.NOSOTROS: ('-ar', '+ábamos'),
            Personal.VOSOTROS: ('-ar', '+abais'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ar', '+aban')
        },
        Tense.INDICATIVE_CONDITIONAL: {
            Personal.YO: ('+ía',),
            Personal.TÚ: ('+ías',),
            Personal.ÉL__ELLA__USTED: ('+ía',),
            Personal.NOSOTROS: ('+íamos',),
            Personal.VOSOTROS: ('+íais',),
            Personal.ELLOS__ELLAS__USTEDES: ('+ían',)
        },
        Tense.INDICATIVE_FUTURE: {
            Personal.YO: ('+é',),
            Personal.TÚ: ('+ás',),
            Personal.ÉL__ELLA__USTED: ('+á',),
            Personal.NOSOTROS: ('+emos',),
            Personal.VOSOTROS: ('+éis',),
            Personal.ELLOS__ELLAS__USTEDES: ('+án',)
        },
        Tense.SUBJUNCTIVE_PRESENT: {
            Personal.YO: ('-ar', '+e'),
            Personal.TÚ: ('-ar', '+es'),
            Personal.ÉL__ELLA__USTED: ('-ar', '+e'),
            Personal.NOSOTROS: ('-ar', '+emos'),
            Personal.VOSOTROS: ('-ar', '+éis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ar', '+en')
        },
        Tense.SUBJUNCTIVE_IMPERFECT_1: {
            Personal.YO: ('-ron', '+ra'),
            Personal.TÚ: ('-ron', '+ras'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+ra'),
            Personal.NOSOTROS: ('-ron', '/s', '+ramos'),
            Personal.VOSOTROS: ('-ron', '+rais'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+ran')
        },
        Tense.SUBJUNCTIVE_IMPERFECT_2: {
            Personal.YO: ('-ron', '+se'),
            Personal.TÚ: ('-ron', '+ses'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+se'),
            Personal.NOSOTROS: ('-ron', '/s', '+semos'),
            Personal.VOSOTROS: ('-ron', '+seis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+sen')
        },
        Tense.SUBJUNCTIVE_FUTURE: {
            Personal.YO: ('-ron', '+re'),
            Personal.TÚ: ('-ron', '+res'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+re'),
            Personal.NOSOTROS: ('-ron', '/s', '+remos'),
            Personal.VOSOTROS: ('-ron', '+reis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+ren')
        },
        Tense.IMPERATIVE_AFFIRMATIVE: {
            Personal.TÚ: ('-o', '+a'),
            Personal.ÉL__ELLA__USTED: ('-o', '+e'),
            Personal.NOSOTROS: ('-o', '+emos'),
            Personal.VOSOTROS: ('-o', '+ad'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+en')
        },
        Tense.IMPERATIVE_NEGATIVE: {
            Personal.TÚ: (':no ', '-ar', '+es'),
            Personal.ÉL__ELLA__USTED: (':no ', '-ar', '+e'),
            Personal.NOSOTROS: (':no ', '-ar', '+emos'),
            Personal.VOSOTROS: (':no ', '-ar', '+éis'),
            Personal.ELLOS__ELLAS__USTEDES: (':no ', '-ar', '+en')
        }
    }
    # the er-verb
    ER = {}
    # the ir-verb
    IR = {}
    # the ar-reflexive-verb
    ARSE = {}
    # the er-reflexive-verb
    ERSE = {}
    # the ir-reflexive-verb
    IRSE = {}
    # not a verb
    NOT_VERB = {}

    # check the type of the passed-in verb (ar/er/ir/arse/erse/irse)
    # noinspection PyTypeChecker
    @staticmethod
    def check_verb_type(inf: str):
        # check all the verb-types except for 'not-verb'
        for verb_type in list(VerbType):
            if verb_type != VerbType.NOT_VERB and inf.lower().endswith(verb_type.name.lower()):
                return verb_type
        # no result after checking all verb-types, it's not a verb
        return VerbType.NOT_VERB

    # conjugate a certain verb as the designated tense & personal
    def get_conjugated(self, form: str, tense: Tense, personal: Personal):
        method = self.__get_conjugating_method(tense, personal)
        lis = list(form)
        if method is not None:
            for cmd in method:
                # remove some characters from the tail of the form
                if cmd[0] == '-':
                    if ''.join(lis).endswith(cmd[1:]):
                        lis = lis[:-(len(cmd) - 1)]
                    else:
                        return False, ''
                # concatenate some characters into the tail of the form
                elif cmd[0] == '+':
                    lis.extend(cmd[1:])
                # add some character at the head of the form
                elif cmd[0] == ':':
                    lis = list(cmd[1:] + ''.join(lis))
                # stress the last character if it's a vowel
                elif cmd == '/s':
                    lis[-1] = CharChecker.to_stressed(lis[-1])
            return True, ''.join(lis)
        else:
            return False, ''

    # get the conjugating method according to the different type of verb
    def __get_conjugating_method(self, tense: Tense, personal: Personal):
        if tense in self.value and personal in self.value[tense]:
            return self.value[tense][personal]
        return None
