import sys
import unittest
from applyRegEx import *


class Lab06TestSuite(unittest.TestCase):

    def test_checkPythonVersion(self):

        currentVersion = sys.version_info
        self.assertGreaterEqual(currentVersion, (3, 4))

    def test_isSplitUsed(self):

        with open("applyRegEx.py", "r") as pyFile:
            sourceCode = pyFile.read()

        self.assertFalse(".split(" in sourceCode)

    def test_getRejectedUsers(self):
        expectedValue = RegularExpressionData.rejectedUsers
        actualValue = getRejectedUsers()

        self.assertListEqual(actualValue, expectedValue)

    def test_getUsersWithCompleteInfo(self):
        expectedValue = RegularExpressionData.completeUsers
        actualValue = getUsersWithCompleteInfo()

        self.assertDictEqual(actualValue, expectedValue)

    def test_getUsersWithEmails(self):
        expectedValue = RegularExpressionData.usersWithEmails
        actualValue = getUsersWithEmails()

        self.assertDictEqual(actualValue, expectedValue)

    def test_getUsersWithPhones(self):
        expectedValue = RegularExpressionData.usersWithPhones
        actualValue = getUsersWithPhones()

        self.assertDictEqual(actualValue, expectedValue)

    def test_getUsersWithStates(self):
        expectedValue = RegularExpressionData.usersWithStates
        actualValue = getUsersWithStates()

        self.assertDictEqual(actualValue, expectedValue)

    def test_getUsersWithoutEmails(self):
        expectedValue = RegularExpressionData.usersWithoutEmails
        actualValue = getUsersWithoutEmails()

        self.assertListEqual(actualValue, expectedValue)

    def test_getUsersWithoutPhones(self):
        expectedValue = RegularExpressionData.usersWithoutPhones
        actualValue = getUsersWithoutPhones()

        self.assertListEqual(actualValue, expectedValue)

    def test_getUsersWithoutStates(self):
        expectedValue = RegularExpressionData.usersWithoutStates
        actualValue = getUsersWithoutStates()

        self.assertListEqual(actualValue, expectedValue)


class RegularExpressionData:
    
    completeUsers = {'Ada Houston': ('ada_houston@purdue.com', '(937) 301-5392', 'Ohio'),
                     'Allen Bryan': ('allen.bryan@purdue.com', '(605) 919-9928', 'South Dakota'),
                     'Angela Banks': ('angela.banks@purdue.com', '(442) 671-3681', 'California'),
                     'Bates Patrick': ('bates_patrick@purdue.com', '(224) 471-3886', 'Illinois'),
                     'Benson Allen': ('benson_allen@purdue.com', '(916) 552-6302', 'California'),
                     'Cameron Rice': ('cameron_rice@purdue.com', '(252) 391-8999', 'North Carolina'),
                     'Campbell Benson': ('campbell_benson@purdue.com', '(331) 518-9491', 'Illinois'),
                     'Carmen Daniels': ('carmen_daniels@purdue.com', '(325) 625-9448', 'Texas'),
                     'Cary Wade': ('cary.wade@purdue.com', '(256) 252-1554', 'Alabama'),
                     'Casey Russell': ('casey_russell@purdue.com', '(815) 261-5888', 'Illinois'),
                     'Cecil Ryan': ('cecil.ryan@purdue.com', '(856) 459-8009', 'New Jersey'),
                     'Charlie Mccormick': ('charlie.mccormick@purdue.com', '(435) 696-2917', 'Utah'),
                     'Chester Tucker': ('chester.tucker@purdue.com', '(319) 584-7285', 'Iowa'),
                     'Clifton Webb': ('clifton_webb@purdue.com', '(561) 531-3711', 'Florida'),
                     'Courtney Garner': ('cgarner607@purdue.com', '(607) 153-3577', 'New York'),
                     'Dale Johnson': ('djohnson216@purdue.com', '(404) 914-1279', 'Georgia'),
                     'Darrell Fleming': ('dfleming386@purdue.com', '(720) 661-9969', 'Colorado'),
                     'Davidson Murphy': ('davidson.murphy@purdue.com', '(254) 748-1660', 'Texas'),
                     'Derrick Byrd': ('derrick_byrd@purdue.com', '(651) 300-3260', 'Minnesota'),
                     'Dunn Melinda': ('dmelinda405@purdue.com', '(859) 964-4796', 'Kentucky'),
                     'Earnest Hudson': ('ehudson398@purdue.com', '(316) 123-4148', 'Kansas'),
                     'Elvira Clarke': ('elvira_clarke@purdue.com', '(619) 747-2237', 'California'),
                     'Frances Larson': ('flarson951@purdue.com', '(915) 972-9723', 'Texas'),
                     'Ginger Long': ('glong516@purdue.com', '(910) 157-6021', 'North Carolina'),
                     'Green Campbell': ('gcampbell249@purdue.com', '(901) 479-6387', 'Tennessee'),
                     'Gwendolyn Houston': ('ghouston967@purdue.com', '(878) 786-1818', 'Pennsylvania'),
                     'Hattie Marshall': ('hattie.marshall@purdue.com', '(419) 441-2099', 'Ohio'),
                     'Houston Calvin': ('houston_calvin@purdue.com', '(979) 688-4521', 'Texas'),
                     'James Hicks': ('james_hicks@purdue.com', '(947) 615-9071', 'Michigan'),
                     'Joanna King': ('jking308@purdue.com', '(225) 834-8539', 'Louisiana'),
                     'Joanna Moody': ('jmoody537@purdue.com', '(540) 856-4924', 'Virginia'),
                     'Joanne Craig': ('jcraig951@purdue.com', '(763) 820-4455', 'Minnesota'),
                     'Jody Richards': ('jody.richards@purdue.com', '(567) 572-7026', 'Ohio'),
                     'Joyce Adkins': ('jadkins960@purdue.com', '(508) 911-7771', 'Massachusetts'),
                     'Larson Winifred': ('larson.winifred@purdue.com', '(228) 673-8939', 'Mississippi'),
                     'Lisa Douglas': ('lisa.douglas@purdue.com', '(701) 863-3758', 'North Dakota'),
                     'Lowell Marshall': ('lowell_marshall@purdue.com', '(203) 405-7072', 'Connecticut'),
                     'Lynda Aguilar': ('lynda_aguilar@purdue.com', '(803) 446-3854', 'South Carolina'),
                     'Lynette Richardson': ('lynette_richardson@purdue.com', '(304) 418-8550', 'West Virginia'),
                     'Matt Day': ('matt_day@purdue.com', '(713) 175-7724', 'Texas'),
                     'May Jacobs': ('may_jacobs@purdue.com', '(423) 310-7162', 'Tennessee'),
                     'May Kathleen': ('may_kathleen@purdue.com', '(610) 325-3644', 'Pennsylvania'),
                     'Melinda Santiago': ('melinda_santiago@purdue.com', '(219) 562-8552', 'Indiana'),
                     'Meredith Martin': ('mmartin931@purdue.com', '(678) 845-2559', 'Georgia'),
                     'Michael Hopkins': ('mhopkins306@purdue.com', '(740) 378-9869', 'Ohio'),
                     'Murphy Gwendolyn': ('murphy_gwendolyn@purdue.com', '(520) 332-9591', 'Arizona'),
                     'Otis Wade': ('otis.wade@purdue.com', '(207) 839-2714', 'Maine'),
                     'Patrick Bates': ('pbates940@purdue.com', '(707) 427-2837', 'California'),
                     'Phillip Elliott': ('phillip_elliott@purdue.com', '(484) 750-1750', 'Pennsylvania'),
                     'Richardson Melinda': ('richardson.melinda@purdue.com', '(417) 911-4213', 'Missouri'),
                     'Robertson Molly': ('rmolly760@purdue.com', '(808) 436-3787', 'Hawaii'),
                     'Russell Ginger': ('russell_ginger@purdue.com', '(320) 964-1535', 'Minnesota'),
                     'Sandra Robertson': ('srobertson878@purdue.com', '(980) 762-6763', 'North Carolina'),
                     'Sims Elbert': ('sims.elbert@purdue.com', '(215) 605-4515', 'Pennsylvania'),
                     'Terri Adkins': ('terri.adkins@purdue.com', '(906) 427-2615', 'Michigan'),
                     'Tyrone Watson': ('tyrone_watson@purdue.com', '(940) 797-3581', 'Texas'),
                     'Vicki Clark': ('vicki_clark@purdue.com', '(626) 877-5646', 'California'),
                     'Warner Joanna': ('wjoanna658@purdue.com', '(339) 714-3248', 'Massachusetts'),
                     'Watkins Chester': ('watkins.chester@purdue.com', '(718) 500-6831', 'New York'),
                     'Watson Warren': ('watson.warren@purdue.com', '(857) 623-7591', 'Massachusetts'),
                     'Winifred Watkins': ('wwatkins317@purdue.com', '(480) 804-3635', 'Arizona')}

    rejectedUsers = ['Clark Jody', 'Earnest Day', 'Evelyn Rice', 'Hattie Campbell', 'Joyce Norris', 'Lucille Mann',
                     'Lula Thomas', 'Miller Curtis', 'Omar Olson']

    usersWithEmails = {'Darrell Fleming': 'dfleming386@purdue.com', 'Hattie Marshall': 'hattie.marshall@purdue.com',
                       'Vicki Russell': 'vrussell499@purdue.com', 'Terry Clarke': 'terry.clarke@purdue.com',
                       'Delbert Buchanan': 'dbuchanan140@purdue.com', 'Nelson Mills': 'nelson.mills@purdue.com',
                       'Cecil Ryan': 'cecil.ryan@purdue.com', 'James Hicks': 'james_hicks@purdue.com',
                       'Allen Bryan': 'allen.bryan@purdue.com', 'Lowell Marshall': 'lowell_marshall@purdue.com',
                       'Garry Nelson': 'garry_nelson@purdue.com', 'Larson Winifred': 'larson.winifred@purdue.com',
                       'Alma Powell': 'apowell343@purdue.com', 'Teresa Roy': 'teresa_roy@purdue.com',
                       'Earnest Hudson': 'ehudson398@purdue.com', 'Baker Terri': 'bterri901@purdue.com',
                       'Moody Morris': 'moody_morris@purdue.com', 'Jody Richards': 'jody.richards@purdue.com',
                       'Mills Palmer': 'mpalmer974@purdue.com', 'Phillip Mann': 'phillip.mann@purdue.com',
                       'Dunn Melinda': 'dmelinda405@purdue.com', 'Murphy Gwendolyn': 'murphy_gwendolyn@purdue.com',
                       'Courtney Garner': 'cgarner607@purdue.com', 'Kara Singleton': 'kara_singleton@purdue.com',
                       'Ginger Parker': 'ginger_parker@purdue.com', 'Ada Houston': 'ada_houston@purdue.com',
                       'Joanne Daniels': 'joanne.daniels@purdue.com', 'Dale Johnson': 'djohnson216@purdue.com',
                       'Tami Green': 'tgreen279@purdue.com', 'Joanne Craig': 'jcraig951@purdue.com',
                       'Nina Richardson': 'nrichardson223@purdue.com', 'Curtis Casey': 'curtis.casey@purdue.com',
                       'Cameron Rice': 'cameron_rice@purdue.com', 'Bates Patrick': 'bates_patrick@purdue.com',
                       'Bass Davidson': 'bass_davidson@purdue.com', 'Kathy Norman': 'kathy_norman@purdue.com',
                       'Mann Alma': 'malma825@purdue.com', 'Calvin Moore': 'calvin.moore@purdue.com',
                       'Adkins Jeffery': 'ajeffery805@purdue.com',
                       'Richardson Melinda': 'richardson.melinda@purdue.com',
                       'Benson Allen': 'benson_allen@purdue.com', 'Stacy Wise': 'stacy.wise@purdue.com',
                       'Meredith Martin': 'mmartin931@purdue.com', 'Ginger Long': 'glong516@purdue.com',
                       'Yates Lorena': 'yates_lorena@purdue.com', 'James Dunn': 'jdunn780@purdue.com',
                       'Joanna Moody': 'jmoody537@purdue.com', 'Kurt Elliott': 'kurt.elliott@purdue.com',
                       'Russell Ginger': 'russell_ginger@purdue.com', 'Lucille Hernandez': 'lhernandez243@purdue.com',
                       'May Jacobs': 'may_jacobs@purdue.com', 'Anthony Wise': 'anthony_wise@purdue.com',
                       'Jared Higgins': 'jared_higgins@purdue.com', 'Nelson Craig': 'ncraig311@purdue.com',
                       'Carter Terry': 'carter_terry@purdue.com', 'Olive Bryan': 'obryan118@purdue.com',
                       'Jamie Spencer': 'jamie_spencer@purdue.com', 'Patrick Bates': 'pbates940@purdue.com',
                       'Derrick Barber': 'derrick.barber@purdue.com', 'Frances Larson': 'flarson951@purdue.com',
                       'Sims Elbert': 'sims.elbert@purdue.com', 'Gina Adams': 'gadams166@purdue.com',
                       'Casey Russell': 'casey_russell@purdue.com', 'Cary Wade': 'cary.wade@purdue.com',
                       'Abraham Evans': 'abraham_evans@purdue.com', 'Jeanne Ryan': 'jryan910@purdue.com',
                       'Matt Day': 'matt_day@purdue.com', 'Joanna King': 'jking308@purdue.com',
                       'Carmen Daniels': 'carmen_daniels@purdue.com', 'Houston Calvin': 'houston_calvin@purdue.com',
                       'Day Dale': 'day_dale@purdue.com', 'Watson Warren': 'watson.warren@purdue.com',
                       'Rogers Ryan': 'rogers.ryan@purdue.com', 'Robertson Molly': 'rmolly760@purdue.com',
                       'Otis Wade': 'otis.wade@purdue.com', 'Angela Banks': 'angela.banks@purdue.com',
                       'Delia Long': 'delia.long@purdue.com', 'Warner Joanna': 'wjoanna658@purdue.com',
                       'Chester Tucker': 'chester.tucker@purdue.com', 'Watkins Chester': 'watkins.chester@purdue.com',
                       'Sandra Robertson': 'srobertson878@purdue.com', 'Orville Lowe': 'orville_lowe@purdue.com',
                       'Campbell Benson': 'campbell_benson@purdue.com', 'Valerie Mills': 'valerie_mills@purdue.com',
                       'Terri Adkins': 'terri.adkins@purdue.com', 'Beck Jeanne': 'beck_jeanne@purdue.com',
                       'Snyder Otis': 'snyder.otis@purdue.com', 'Singleton Mercedes': 'singleton_mercedes@purdue.com',
                       'Hudson Evelyn': 'hevelyn969@purdue.com', 'Terry Douglas': 'terry.douglas@purdue.com',
                       'Fleming Bass': 'fleming.bass@purdue.com', 'Charlie Mccormick': 'charlie.mccormick@purdue.com',
                       'Bradford Alexander': 'bradford.alexander@purdue.com', 'Vicki Clark': 'vicki_clark@purdue.com',
                       'Phillip Elliott': 'phillip_elliott@purdue.com', 'Lisa Douglas': 'lisa.douglas@purdue.com',
                       'Kurt Adams': 'kurt.adams@purdue.com', 'Gwendolyn Houston': 'ghouston967@purdue.com',
                       'Vanessa Olson': 'volson596@purdue.com', 'Santiago Clifton': 'sclifton706@purdue.com',
                       'Terri Beck': 'tbeck916@purdue.com', 'Gwendolyn Goodwin': 'gwendolyn_goodwin@purdue.com',
                       'Andre Powell': 'andre_powell@purdue.com', 'Lula Matthews': 'lmatthews51@purdue.com',
                       'Tyrone Watson': 'tyrone_watson@purdue.com', 'Michael Hopkins': 'mhopkins306@purdue.com',
                       'Jenny Greene': 'jgreene883@purdue.com', 'Winifred Watkins': 'wwatkins317@purdue.com',
                       'Cain Abraham': 'cain_abraham@purdue.com', 'Stone Carmen': 'stone.carmen@purdue.com',
                       'Nelson Garry': 'nelson.garry@purdue.com',
                       'Lynette Richardson': 'lynette_richardson@purdue.com',
                       'Elvira Clarke': 'elvira_clarke@purdue.com', 'Davidson Murphy': 'davidson.murphy@purdue.com',
                       'Clifton Webb': 'clifton_webb@purdue.com', 'Pat Byrd': 'pbyrd669@purdue.com',
                       'May Kathleen': 'may_kathleen@purdue.com', 'Joyce Adkins': 'jadkins960@purdue.com',
                       'Melinda Santiago': 'melinda_santiago@purdue.com', 'Molly Bass': 'molly.bass@purdue.com',
                       'Kristen Bates': 'kristen_bates@purdue.com', 'Green Campbell': 'gcampbell249@purdue.com',
                       'Derrick Byrd': 'derrick_byrd@purdue.com', 'Nina Patrick': 'npatrick359@purdue.com',
                       'Lynda Aguilar': 'lynda_aguilar@purdue.com', 'Lorena Parker': 'lparker309@purdue.com',
                       'Shannon Thomas': 'shannon.thomas@purdue.com', 'Meredith Morris': 'meredith_morris@purdue.com',
                       'Omar Yates': 'oyates54@purdue.com'}

    usersWithPhones = {'Ada Houston': '(937) 301-5392', 'Darrell Fleming': '(720) 661-9969',
                       'Hattie Marshall': '(419) 441-2099', 'Nina Richardson': '(702) 340-9643',
                       'Mann Alma': '(432) 129-5058', 'Murphy Gwendolyn': '(520) 332-9591',
                       'Nelson Mills': '(931) 799-3943', 'Cecil Ryan': '(856) 459-8009',
                       'James Hicks': '(947) 615-9071', 'Allen Bryan': '(605) 919-9928',
                       'Lowell Marshall': '(203) 405-7072', 'Garry Nelson': '(641) 763-3173',
                       'Larson Winifred': '(228) 673-8939', 'Carmen Daniels': '(325) 625-9448',
                       'Teresa Roy': '(314) 424-5042', 'Earnest Hudson': '(316) 123-4148',
                       'Baker Terri': '(603) 365-2889', 'Elena Lowe': '(478) 903-5486',
                       'Campbell Benson': '(331) 518-9491', 'Jody Richards': '(567) 572-7026',
                       'Ada Kennedy': '(308) 747-6923', 'Dunn Melinda': '(859) 964-4796',
                       'Casey Carter': '(323) 465-3673', 'Courtney Garner': '(607) 153-3577',
                       'Kara Singleton': '(574) 925-8290', 'Ginger Parker': '(716) 977-8548',
                       'Evelyn Sims': '(307) 756-6522', 'Jeffery Stokes': '(602) 387-6519',
                       'Dale Johnson': '(404) 914-1279', 'Ryan Sandra': '(918) 485-9664',
                       'Joanne Craig': '(763) 820-4455', 'Elena Goodwin': '(502) 502-4464',
                       'Curtis Casey': '(917) 854-5300', 'Cameron Rice': '(252) 391-8999',
                       'Jeffery Alexander': '(206) 517-8020', 'Bates Patrick': '(224) 471-3886',
                       'Kathy Norman': '(724) 342-7390', 'Charlie Mccormick': '(435) 696-2917',
                       'Calvin Miller': '(315) 101-4385', 'Richardson Melinda': '(417) 911-4213',
                       'Benson Allen': '(916) 552-6302', 'Meredith Martin': '(678) 845-2559',
                       'Ginger Long': '(910) 157-6021', 'Joanna Moody': '(540) 856-4924',
                       'Robertson Molly': '(808) 436-3787', 'Owen Green': '(475) 696-7947',
                       'Kurt Elliott': '(270) 452-2768', 'Russell Ginger': '(320) 964-1535',
                       'May Jacobs': '(423) 310-7162', 'Erika Allen': '(231) 609-3607',
                       'Watson Warren': '(857) 623-7591', 'Phillip Elliott': '(484) 750-1750',
                       'Angela Campbell': '(501) 909-9242', 'Patrick Bates': '(707) 427-2837',
                       'Brandy Alvarez': '(787) 783-1618', 'Derrick Barber': '(305) 145-9317',
                       'Frances Larson': '(915) 972-9723', 'Sims Elbert': '(215) 605-4515',
                       'Delia Powers': '(913) 777-5096', 'Gina Adams': '(340) 683-4600',
                       'Ryan Lambert': '(732) 628-8228', 'Casey Russell': '(815) 261-5888',
                       'Jesus Norris': '(765) 506-7428', 'Cary Wade': '(256) 252-1554',
                       'Jeanne Ryan': '(205) 181-6244', 'Matt Day': '(713) 175-7724',
                       'Joanna King': '(225) 834-8539', 'Lillie Lynch': '(360) 967-7480',
                       'Houston Calvin': '(979) 688-4521', 'Shannon Sims': '(850) 767-6112',
                       'Toni Curtis': '(909) 669-5317', 'Powers Elena': '(240) 405-9288',
                       'Max Matthews': '(512) 640-3652', 'Wayne Evans': '(757) 305-2377',
                       'Kathleen Valdez': '(681) 623-4500', 'Otis Wade': '(207) 839-2714',
                       'Angela Banks': '(442) 671-3681', 'Watkins Chester': '(718) 500-6831',
                       'Warner Joanna': '(339) 714-3248', 'Chester Tucker': '(319) 584-7285',
                       'Roy Tami': '(608) 235-7475', 'Palmer Earnest': '(570) 464-3846',
                       'Stacy Bryan': '(623) 321-6840', 'Morris James': '(704) 133-7635',
                       'Mercedes Cain': '(571) 581-1242', 'Jody Larson': '(430) 412-6637',
                       'Terri Adkins': '(906) 427-2615', 'Kenny Kennedy': '(505) 629-3959',
                       'Singleton Mercedes': '(928) 734-1584', 'Hudson Evelyn': '(719) 702-6986',
                       'Wayne Delgado': '(973) 864-7601', 'Dale Powers': '(218) 765-6524',
                       'Jared Roy': '(907) 710-7144', 'Sandra Robertson': '(980) 762-6763',
                       'Lynch Anthony': '(541) 114-8361', 'Craig Andre': '(870) 828-4596',
                       'Webb Nelson': '(303) 156-1383', 'Lisa Douglas': '(701) 863-3758',
                       'Morris Morris': '(661) 685-6063', 'Gwendolyn Houston': '(878) 786-1818',
                       'Spencer Stacy': '(302) 548-2634', 'Gwendolyn Goodwin': '(734) 575-6003',
                       'Andre Powell': '(312) 309-9176', 'Lorena Parker': '(585) 650-8991',
                       'Tyrone Watson': '(940) 797-3581', 'Vicki Clark': '(626) 877-5646',
                       'Michael Hopkins': '(740) 378-9869', 'Harvey Omar': '(760) 184-9404',
                       'Bryan Tami': '(507) 550-9450', 'Winifred Watkins': '(480) 804-3635',
                       'Mills Palmer': '(773) 301-5794', 'Erika Bass': '(402) 260-3096',
                       'Jenna Moody': '(650) 595-2410', 'Jenny Harvey': '(786) 875-1030',
                       'Nelson Garry': '(936) 837-6240', 'Elbert Beck': '(954) 398-6735',
                       'Shannon Thomas': '(872) 155-5226', 'Lynette Richardson': '(304) 418-8550',
                       'Elvira Clarke': '(619) 747-2237', 'Jeanne Palmer': '(845) 458-1173',
                       'Davidson Murphy': '(254) 748-1660', 'Clifton Webb': '(561) 531-3711',
                       'Pat Byrd': '(774) 810-6695', 'May Kathleen': '(610) 325-3644',
                       'Joyce Adkins': '(508) 911-7771', 'Melinda Santiago': '(219) 562-8552',
                       'Green Campbell': '(901) 479-6387', 'Derrick Byrd': '(651) 300-3260',
                       'Vanessa Olson': '(330) 113-2423', 'Lynda Aguilar': '(803) 446-3854',
                       'Garry Barber': '(214) 799-6165', 'Norris Gina': '(301) 175-5641'}

    usersWithStates = {'Ada Houston': 'Ohio', 'Darrell Fleming': 'Colorado', 'Hattie Marshall': 'Ohio',
                       'Delbert Buchanan': 'North Carolina', 'Cecil Ryan': 'New Jersey', 'James Hicks': 'Michigan',
                       'Allen Bryan': 'South Dakota', 'Ruby Baker': 'Florida', 'Lowell Marshall': 'Connecticut',
                       'Ryan Lambert': 'New Jersey', 'Larson Winifred': 'Mississippi', 'Alma Powell': 'Maryland',
                       'Earnest Hudson': 'Kansas', 'Joanna King': 'Louisiana', 'Roy Tami': 'Wisconsin',
                       'Moody Morris': 'California', 'Jody Richards': 'Ohio', 'Ada Kennedy': 'Nebraska',
                       'Phillip Mann': 'California', 'Dunn Melinda': 'Kentucky', 'Bryant Benson': 'Texas',
                       'Casey Carter': 'California', 'Murphy Gwendolyn': 'Arizona', 'Courtney Garner': 'New York',
                       'Delbert Warner': 'California', 'Evelyn Sims': 'Wyoming', 'Jeffery Stokes': 'Arizona',
                       'Dale Johnson': 'Georgia', 'Ryan Sandra': 'Oklahoma', 'Joanne Craig': 'Minnesota',
                       'Elena Goodwin': 'Kentucky', 'Cameron Rice': 'North Carolina',
                       'Jeffery Alexander': 'Washington', 'Bates Patrick': 'Illinois', 'Carmen Daniels': 'Texas',
                       'Calvin Moore': 'Virginia', 'Calvin Miller': 'New York', 'Carter Terry': 'Rhode Island',
                       'Richardson Melinda': 'Missouri', 'Benson Allen': 'California',
                       'Abraham Greene': 'Pennsylvania', 'Meredith Martin': 'Georgia',
                       'Ginger Long': 'North Carolina', 'Molly Alvarez': 'Florida', 'Lula Matthews': 'Georgia',
                       'Joanna Moody': 'Virginia', 'Russell Ginger': 'Minnesota', 'Lucille Hernandez': 'Wisconsin',
                       'Otis Murphy': 'South Carolina', 'Erika Allen': 'Michigan', 'Jared Higgins': 'Utah',
                       'Adkins Jeffery': 'Kansas', 'Jenna Garner': 'Illinois', 'Olive Bryan': 'Iowa',
                       'Jamie Spencer': 'Oklahoma', 'Patrick Bates': 'California', 'Brandy Alvarez': 'Puerto Rico',
                       'Frances Larson': 'Texas', 'Sims Elbert': 'Pennsylvania', 'Delia Powers': 'Kansas',
                       'Shannon Sims': 'Florida', 'Casey Russell': 'Illinois', 'Jesus Norris': 'Indiana',
                       'Angela Campbell': 'Arkansas', 'Cary Wade': 'Alabama', 'Abraham Evans': 'Alabama',
                       'Robertson Molly': 'Hawaii', 'Dale Powers': 'Minnesota', 'Day Dale': 'Puerto Rico',
                       'Lillie Lynch': 'Washington', 'Houston Calvin': 'Texas', 'Tami Green': 'Illinois',
                       'Watson Warren': 'Massachusetts', 'Rogers Ryan': 'New York', 'Max Matthews': 'Texas',
                       'May Jacobs': 'Tennessee', 'Otis Wade': 'Maine', 'Vicki Clark': 'California',
                       'Watkins Chester': 'New York', 'Warner Joanna': 'Massachusetts', 'Chester Tucker': 'Iowa',
                       'Delia Long': 'Michigan', 'Sandra Robertson': 'North Carolina', 'Stacy Bryan': 'Arizona',
                       'Morris James': 'North Carolina', 'Mercedes Cain': 'Virginia', 'Valerie Mills': 'Florida',
                       'Terri Adkins': 'Michigan', 'Beck Jeanne': 'New York', 'Snyder Otis': 'Arkansas',
                       'Nina Patrick': 'California', 'Terry Douglas': 'Washington', 'Harvey Omar': 'California',
                       'Melinda Santiago': 'Indiana', 'Teresa Buchanan': 'Florida', 'Charlie Mccormick': 'Utah',
                       'Stacy Wise': 'Utah', 'Valerie Warren': 'Michigan', 'Phillip Elliott': 'Pennsylvania',
                       'Lisa Douglas': 'North Dakota', 'Morris Morris': 'California', 'Kurt Adams': 'Massachusetts',
                       'Gwendolyn Houston': 'Pennsylvania', 'Spencer Stacy': 'Delaware',
                       'Santiago Clifton': 'Oklahoma', 'Adams Phillip': 'California', 'Angela Banks': 'California',
                       'Tami Snyder': 'North Carolina', 'Matt Day': 'Texas', 'Lowell Carter': 'Virginia',
                       'Tyrone Watson': 'Texas', 'Jody Larson': 'Texas', 'Michael Hopkins': 'Ohio',
                       'Craig Andre': 'Arkansas', 'Bryan Tami': 'Minnesota', 'Winifred Watkins': 'Arizona',
                       'Warren Spencer': 'California', 'Cain Abraham': 'Michigan', 'Stone Carmen': 'New Mexico',
                       'Jenna Moody': 'California', 'Campbell Benson': 'Illinois', 'Garry Barber': 'Texas',
                       'Lynette Richardson': 'West Virginia', 'Elvira Clarke': 'California',
                       'Davidson Murphy': 'Texas', 'Clifton Webb': 'Florida', 'Daniels Russell': 'Missouri',
                       'May Kathleen': 'Pennsylvania', 'Joyce Adkins': 'Massachusetts', 'Erika Bass': 'Nebraska',
                       'Green Campbell': 'Tennessee', 'Derrick Byrd': 'Minnesota', 'Lynda Aguilar': 'South Carolina',
                       'Kenny Kennedy': 'New Mexico', 'Norris Gina': 'Maryland', 'Omar Yates': 'California',
                       'Marco Rogers': 'New Jersey'}

    usersWithoutEmails = ['Abraham Greene', 'Ada Kennedy', 'Adams Phillip', 'Angela Campbell', 'Brandy Alvarez',
                          'Bryan Tami', 'Bryant Benson', 'Calvin Miller', 'Casey Carter', 'Craig Andre', 'Dale Powers',
                          'Daniels Russell', 'Delbert Warner', 'Delia Powers', 'Elbert Beck', 'Elena Goodwin',
                          'Elena Lowe', 'Erika Allen', 'Erika Bass', 'Evelyn Sims', 'Garry Barber', 'Harvey Omar',
                          'Jared Roy', 'Jeanne Palmer', 'Jeffery Alexander', 'Jeffery Stokes', 'Jenna Garner',
                          'Jenna Moody', 'Jenny Harvey', 'Jesus Norris', 'Jody Larson', 'Kathleen Valdez',
                          'Kenny Kennedy', 'Lillie Lynch', 'Lowell Carter', 'Lynch Anthony', 'Marco Rogers',
                          'Max Matthews', 'Mercedes Cain', 'Molly Alvarez', 'Morris James', 'Morris Morris',
                          'Norris Gina', 'Otis Murphy', 'Owen Green', 'Palmer Earnest', 'Powers Elena', 'Roy Tami',
                          'Ruby Baker', 'Ryan Lambert', 'Ryan Sandra', 'Shannon Sims', 'Spencer Stacy', 'Stacy Bryan',
                          'Tami Snyder', 'Teresa Buchanan', 'Toni Curtis', 'Valerie Warren', 'Warren Spencer',
                          'Wayne Delgado', 'Wayne Evans', 'Webb Nelson']

    usersWithoutPhones = ['Abraham Evans', 'Abraham Greene', 'Adams Phillip', 'Adkins Jeffery', 'Alma Powell',
                          'Anthony Wise', 'Bass Davidson', 'Beck Jeanne', 'Bradford Alexander', 'Bryant Benson',
                          'Cain Abraham', 'Calvin Moore', 'Carter Terry', 'Daniels Russell', 'Day Dale',
                          'Delbert Buchanan', 'Delbert Warner', 'Delia Long', 'Fleming Bass', 'James Dunn',
                          'Jamie Spencer', 'Jared Higgins', 'Jenna Garner', 'Jenny Greene', 'Joanne Daniels',
                          'Kristen Bates', 'Kurt Adams', 'Lowell Carter', 'Lucille Hernandez', 'Lula Matthews',
                          'Marco Rogers', 'Meredith Morris', 'Molly Alvarez', 'Molly Bass', 'Moody Morris',
                          'Nelson Craig', 'Nina Patrick', 'Olive Bryan', 'Omar Yates', 'Orville Lowe', 'Otis Murphy',
                          'Phillip Mann', 'Rogers Ryan', 'Ruby Baker', 'Santiago Clifton', 'Snyder Otis', 'Stacy Wise',
                          'Stone Carmen', 'Tami Green', 'Tami Snyder', 'Teresa Buchanan', 'Terri Beck', 'Terry Clarke',
                          'Terry Douglas', 'Valerie Mills', 'Valerie Warren', 'Vicki Russell', 'Warren Spencer',
                          'Yates Lorena']

    usersWithoutStates = ['Andre Powell', 'Anthony Wise', 'Baker Terri', 'Bass Davidson', 'Bradford Alexander',
                          'Curtis Casey', 'Derrick Barber', 'Elbert Beck', 'Elena Lowe', 'Fleming Bass', 'Garry Nelson',
                          'Gina Adams', 'Ginger Parker', 'Gwendolyn Goodwin', 'Hudson Evelyn', 'James Dunn',
                          'Jared Roy', 'Jeanne Palmer', 'Jeanne Ryan', 'Jenny Greene', 'Jenny Harvey', 'Joanne Daniels',
                          'Kara Singleton', 'Kathleen Valdez', 'Kathy Norman', 'Kristen Bates', 'Kurt Elliott',
                          'Lorena Parker', 'Lynch Anthony', 'Mann Alma', 'Meredith Morris', 'Mills Palmer',
                          'Molly Bass', 'Nelson Craig', 'Nelson Garry', 'Nelson Mills', 'Nina Richardson',
                          'Orville Lowe', 'Owen Green', 'Palmer Earnest', 'Pat Byrd', 'Powers Elena', 'Shannon Thomas',
                          'Singleton Mercedes', 'Teresa Roy', 'Terri Beck', 'Terry Clarke', 'Toni Curtis',
                          'Vanessa Olson', 'Vicki Russell', 'Wayne Delgado', 'Wayne Evans', 'Webb Nelson',
                          'Yates Lorena']

if __name__ == '__main__':
    unittest.main()
