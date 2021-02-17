from enum import Enum

from enums.personal import Personal
from enums.tense import Tense
from utils.character_checker import CharChecker


# noinspection SpellCheckingInspection
class VerbType(Enum):
    """
    iar uar
    aer eer oer (ller ñer)
    aír eír oír uir üir (llir ñir)
    -
    car gar zar guar
    cer ger
    cir gir quir guir
    """
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
            Personal.YO: ('-ar', '+é|gu>gü|g>gu|c>qu|z>c'),
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
            Personal.YO: ('-ar', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.TÚ: ('-ar', '+es|gu>gü|g>gu|c>qu|z>c'),
            Personal.ÉL__ELLA__USTED: ('-ar', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.NOSOTROS: ('-ar', '+emos|gu>gü|g>gu|c>qu|z>c'),
            Personal.VOSOTROS: ('-ar', '+éis|gu>gü|g>gu|c>qu|z>c'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ar', '+en|gu>gü|g>gu|c>qu|z>c')
        },
        Tense.SUBJUNCTIVE_IMPERFECT_1: {
            Personal.YO: ('-ron', '+ra'),
            Personal.TÚ: ('-ron', '+ras'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+ra'),
            Personal.NOSOTROS: ('-ron', '/', '+ramos'),
            Personal.VOSOTROS: ('-ron', '+rais'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+ran')
        },
        Tense.SUBJUNCTIVE_IMPERFECT_2: {
            Personal.YO: ('-ron', '+se'),
            Personal.TÚ: ('-ron', '+ses'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+se'),
            Personal.NOSOTROS: ('-ron', '/', '+semos'),
            Personal.VOSOTROS: ('-ron', '+seis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+sen')
        },
        Tense.SUBJUNCTIVE_FUTURE: {
            Personal.YO: ('-ron', '+re'),
            Personal.TÚ: ('-ron', '+res'),
            Personal.ÉL__ELLA__USTED: ('-ron', '+re'),
            Personal.NOSOTROS: ('-ron', '/', '+remos'),
            Personal.VOSOTROS: ('-ron', '+reis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ron', '+ren')
        },
        Tense.IMPERATIVE_AFFIRMATIVE: {
            Personal.TÚ: ('-o', '+a'),
            Personal.ÉL__ELLA__USTED: ('-o', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.NOSOTROS: ('-o', '+emos|gu>gü|g>gu|c>qu|z>c'),
            Personal.VOSOTROS: ('-o', '+ad'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+en|gu>gü|g>gu|c>qu|z>c')
        },
        Tense.IMPERATIVE_NEGATIVE: {
            Personal.TÚ: (':no ', '-ar', '+es|gu>gü|g>gu|c>qu|z>c'),
            Personal.ÉL__ELLA__USTED: (':no ', '-ar', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.NOSOTROS: (':no ', '-ar', '+emos|gu>gü|g>gu|c>qu|z>c'),
            Personal.VOSOTROS: (':no ', '-ar', '+éis|gu>gü|g>gu|c>qu|z>c'),
            Personal.ELLOS__ELLAS__USTEDES: (':no ', '-ar', '+en|gu>gü|g>gu|c>qu|z>c')
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
        # special case: the verb which ends w/ 'ír'
        if inf.lower().endswith('ír'):
            return VerbType.IR
        # no result after checking all verb-types, it's not a verb
        return VerbType.NOT_VERB

    # conjugate a certain verb as the designated tense & personal
    def get_conjugated(self, form: str, tense: Tense, personal: Personal):
        method = self.__get_conjugating_method(tense, personal)
        lis = list(form)
        spelling_change = None
        if method is not None:
            for cmd in method:
                # split the command into a main command and possibly a list of spelling commands
                main_cmd, *spelling_cmds = cmd.split('|')
                # if there's some spelling-changings
                for spelling_cmd in spelling_cmds:
                    bef, aft = spelling_cmd.split('>')
                    if ''.join(lis).endswith(bef):
                        lis = lis[:-len(bef)]
                        lis.extend(aft)
                        spelling_change = spelling_cmd
                        break
                # remove some characters from the tail of the form
                if main_cmd[0] == '-':
                    if ''.join(lis).endswith(main_cmd[1:]):
                        lis = lis[:-(len(main_cmd) - 1)]
                    else:
                        return False, '', None
                # concatenate some characters into the tail of the form
                elif main_cmd[0] == '+':
                    lis.extend(main_cmd[1:])
                # add some character at the head of the form
                elif main_cmd[0] == ':':
                    lis = list(main_cmd[1:] + ''.join(lis))
                # stress the last character if it's a vowel
                elif main_cmd == '/':
                    lis[-1] = CharChecker.to_stressed(lis[-1])
            return True, ''.join(lis), spelling_change
        else:
            return False, '', None

    # get the conjugating method according to the different type of verb
    def __get_conjugating_method(self, tense: Tense, personal: Personal):
        if tense in self.value and personal in self.value[tense]:
            return self.value[tense][personal]
        return None
