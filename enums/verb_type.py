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
    """ special symbols: + - _ / : | > """
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
            Personal.YO: ('-o', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.TÚ: ('-o', '+es|gu>gü|g>gu|c>qu|z>c'),
            Personal.ÉL__ELLA__USTED: ('-o', '+e|gu>gü|g>gu|c>qu|z>c'),
            Personal.NOSOTROS: ('-o', '+emos|gu>gü|g>gu|c>qu|z>c'),
            Personal.VOSOTROS: ('-o', '+éis|gu>gü|g>gu|c>qu|z>c'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+en|gu>gü|g>gu|c>qu|z>c')
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
            Personal.VOSOTROS: ('-r', '+d'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+en|gu>gü|g>gu|c>qu|z>c')
        },
        Tense.IMPERATIVE_NEGATIVE: {
            Personal.TÚ: (':no ',),
            Personal.ÉL__ELLA__USTED: (':no ',),
            Personal.NOSOTROS: (':no ',),
            Personal.VOSOTROS: (':no ',),
            Personal.ELLOS__ELLAS__USTEDES: (':no ',)
        }
    }
    # the er-verb
    ER = {
        Tense.PARTICLES: {
            Personal.PRESENT_PARTICLE: ('-er', '+i', '|ei>ey|ai>ay|oi>oy|ñi>ñ|lli>ll', '+endo'),
            Personal.PAST_PARTICLE: ('-er', '+i', '|ei>eí|ai>aí|oi>oí', '+do')
        },
        Tense.INDICATIVE_PRESENT: {
            Personal.YO: ('-er', '+o|g>j|ac>azc|oc>ozc|ec>ezc|ic>izc|uc>uzc|c>z|a>ay|o>oy'),
            Personal.TÚ: ('-er', '+es'),
            Personal.ÉL__ELLA__USTED: ('-er', '+e'),
            Personal.NOSOTROS: ('-er', '+emos'),
            Personal.VOSOTROS: ('-er', '+éis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-er', '+en')
        },
        Tense.INDICATIVE_PRETERITE: {
            Personal.YO: ('-er', '+í'),
            Personal.TÚ: ('-er', '+i', '|ai>aí|oi>oí|ei>eí', '+ste'),
            Personal.ÉL__ELLA__USTED: ('-er', '+i', '|ai>ay|oi>oy|ei>ey|ñi>ñ|lli>ll', '+ó'),
            Personal.NOSOTROS: ('-er', '+i', '|ai>aí|oi>oí|ei>eí', '+mos'),
            Personal.VOSOTROS: ('-er', '+i', '|ai>aí|oi>oí|ei>eí', '+steis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-er', '+i', '|ai>ay|oi>oy|ei>ey|ñi>ñ|lli>ll', '+eron')
        },
        Tense.INDICATIVE_IMPERFECT: {
            Personal.YO: ('-er', '+ía'),
            Personal.TÚ: ('-er', '+ías'),
            Personal.ÉL__ELLA__USTED: ('-er', '+ía'),
            Personal.NOSOTROS: ('-er', '+íamos'),
            Personal.VOSOTROS: ('-er', '+íais'),
            Personal.ELLOS__ELLAS__USTEDES: ('-er', '+ían')
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
            Personal.YO: ('-o', '+a'),
            Personal.TÚ: ('-o', '+as'),
            Personal.ÉL__ELLA__USTED: ('-o', '+a'),
            Personal.NOSOTROS: ('-o', '+amos'),
            Personal.VOSOTROS: ('-o', '+áis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+an')
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
            Personal.TÚ: ('-o', '+e|j>g|z>c|zc>c|oy>o|ay>a|aig>a|oig>o|lg>l|sgo>s|g>gu'),
            Personal.ÉL__ELLA__USTED: ('-o', '+a'),
            Personal.NOSOTROS: ('-o', '+amos'),
            Personal.VOSOTROS: ('-r', '+d'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+an')
        },
        Tense.IMPERATIVE_NEGATIVE: {
            Personal.TÚ: (':no ',),
            Personal.ÉL__ELLA__USTED: (':no ',),
            Personal.NOSOTROS: (':no ',),
            Personal.VOSOTROS: (':no ',),
            Personal.ELLOS__ELLAS__USTEDES: (':no ',)
        }
    }
    # the ir-verb
    IR = {
        Tense.PARTICLES: {
            Personal.PRESENT_PARTICLE: ('-r', '|gui>gui|qui>qui|ui>uy|üi>uy|aí>ay|oí>oy|eí>i|ñi>ñ|lli>ll', '+endo'),
            Personal.PAST_PARTICLE: ('-r', '+do')
        },
        Tense.INDICATIVE_PRESENT: {
            Personal.YO: ('-ir_ír', '+o|g>j|gü>guy|gu>g|qu>c|u>uy|ac>azc|oc>ozc|ec>ezc|ic>izc|uc>uzc|c>z|a>aig|o>oig|e>í'),
            Personal.TÚ: ('-ir_ír', '+es|gü>guy|gu>gu|qu>qu|u>uy|o>oy|e>í'),
            Personal.ÉL__ELLA__USTED: ('-ir_ír', '+e|gü>guy|gu>gu|qu>qu|u>uy|o>oy|e>í'),
            Personal.NOSOTROS: ('-r', '+mos'),
            Personal.VOSOTROS: ('-ir_ír', '+ís'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ir_ír', '+en|gü>guy|gu>gu|qu>qu|u>uy|o>oy|e>í')
        },
        Tense.INDICATIVE_PRETERITE: {
            Personal.YO: ('-ir_ír', '+í'),
            Personal.TÚ: ('-ir_ír', '+i', '|ai>aí|oi>oí|ei>eí', '+ste'),
            Personal.ÉL__ELLA__USTED: ('-ir_ír', '+i', '|güi>guy|gui>gui|qui>qui|ui>uy|ai>ay|oi>oy|ei>i|ñi>ñ|lli>ll', '+ó'),
            Personal.NOSOTROS: ('-ir_ír', '+i', '|ai>aí|oi>oí|ei>eí', '+mos'),
            Personal.VOSOTROS: ('-ir_ír', '+i', '|ai>aí|oi>oí|ei>eí', '+steis'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ir_ír', '+i', '|güi>guy|gui>gui|qui>qui|ui>uy|ai>ay|oi>oy|ei>i|ñi>ñ|lli>ll', '+eron')
        },
        Tense.INDICATIVE_IMPERFECT: {
            Personal.YO: ('-ir_ír', '+ía'),
            Personal.TÚ: ('-ir_ír', '+ías'),
            Personal.ÉL__ELLA__USTED: ('-ir_ír', '+ía'),
            Personal.NOSOTROS: ('-ir_ír', '+íamos'),
            Personal.VOSOTROS: ('-ir_ír', '+íais'),
            Personal.ELLOS__ELLAS__USTEDES: ('-ir_ír', '+ían')
        },
        Tense.INDICATIVE_CONDITIONAL: {
            Personal.YO: ('+ía|ír>ir',),
            Personal.TÚ: ('+ías|ír>ir',),
            Personal.ÉL__ELLA__USTED: ('+ía|ír>ir',),
            Personal.NOSOTROS: ('+íamos|ír>ir',),
            Personal.VOSOTROS: ('+íais|ír>ir',),
            Personal.ELLOS__ELLAS__USTEDES: ('+ían|ír>ir',)
        },
        Tense.INDICATIVE_FUTURE: {
            Personal.YO: ('+é|ír>ir',),
            Personal.TÚ: ('+ás|ír>ir',),
            Personal.ÉL__ELLA__USTED: ('+á|ír>ir',),
            Personal.NOSOTROS: ('+emos|ír>ir',),
            Personal.VOSOTROS: ('+éis|ír>ir',),
            Personal.ELLOS__ELLAS__USTEDES: ('+án|ír>ir',)
        },
        Tense.SUBJUNCTIVE_PRESENT: {
            Personal.YO: ('-o', '+a'),
            Personal.TÚ: ('-o', '+as'),
            Personal.ÉL__ELLA__USTED: ('-o', '+a'),
            Personal.NOSOTROS: ('-o', '+amos|u>|í>i'),
            Personal.VOSOTROS: ('-o', '+áis|u>|í>i'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+an')
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
        # '|g>j|gü>guy|gu>g|qu>c|u>uy|ac>azc|oc>ozc|ec>ezc|ic>izc|uc>uzc|c>z|a>aig|o>oig|e>í'
        Tense.IMPERATIVE_AFFIRMATIVE: {
            Personal.TÚ: ('|oy>o', '-o', '+e|j>g|zc>c|z>c|c>qu|aig>a|oig>o|lg>l|sgo>s|g>gu'),
            Personal.ÉL__ELLA__USTED: ('-o', '+a'),
            Personal.NOSOTROS: ('-o', '+amos|u>'),
            Personal.VOSOTROS: ('-r', '+d'),
            Personal.ELLOS__ELLAS__USTEDES: ('-o', '+an')
        },
        Tense.IMPERATIVE_NEGATIVE: {
            Personal.TÚ: (':no ',),
            Personal.ÉL__ELLA__USTED: (':no ',),
            Personal.NOSOTROS: (':no ',),
            Personal.VOSOTROS: (':no ',),
            Personal.ELLOS__ELLAS__USTEDES: (':no ',)
        }
    }
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
                if main_cmd != '':
                    # remove some characters from the tail of the form
                    if main_cmd[0] == '-':
                        for removee in main_cmd[1:].split('_'):
                            if ''.join(lis).endswith(removee):
                                lis = lis[:-len(removee)]
                                break
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
