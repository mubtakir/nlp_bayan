"""
Hybrid Lexer for Bayan Language
محلل معجمي هجين للغة بيان
"""

import re
from enum import Enum, auto

class TokenType(Enum):
    """Token types for Bayan language"""

    # Traditional tokens
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    OPERATOR = auto()
    ASSIGN = auto()
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    SEMICOLON = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    ARROW = auto()
    PIPE = auto()  # For list pattern [H|T]
    AT = auto()  # For decorators @

    # Keywords
    DEF = auto()
    CLASS = auto()
    IF = auto()
    ELSE = auto()
    ELIF = auto()
    FOR = auto()
    WHILE = auto()
    IN = auto()
    PRINT = auto()
    RETURN = auto()
    YIELD = auto()
    BREAK = auto()
    CONTINUE = auto()
    PASS = auto()
    TRUE = auto()
    FALSE = auto()
    NONE = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    SELF = auto()
    SUPER = auto()
    IMPORT = auto()
    FROM = auto()
    AS = auto()
    TRY = auto()
    EXCEPT = auto()
    FINALLY = auto()
    RAISE = auto()
    WITH = auto()

    # Logical tokens
    PREDICATE = auto()
    VARIABLE = auto()
    IMPLIES = auto()
    UNIFY = auto()
    QUERY = auto()
    FACT = auto()
    RULE = auto()
    IS = auto()  # Arithmetic evaluation operator
    CUT = auto()  # Cut operator (!)

    # Async tokens
    ASYNC = auto()
    AWAIT = auto()

    # Hybrid tokens
    HYBRID = auto()
    ENTITY = auto()
    APPLY = auto()
    CONCEPT = auto()
    ONCE = auto()
    LIMIT = auto()
    MATCH = auto()

    # Temporal tokens
    TEMPORAL = auto()
    WITHIN = auto()
    SCHEDULE = auto()
    DELAY = auto()
    EVERY = auto()
    SECONDS = auto()
    MINUTES = auto()
    HOURS = auto()
    FIRST = auto()
    THEN = auto()
    LASTLY = auto()  # Changed from FINALLY to avoid conflict with try/finally

    # Constraint tokens
    WHERE = auto()
    REQUIRES = auto()
    ENSURES = auto()
    INVARIANT = auto()

    # Pattern matching tokens (MATCH already defined above for match...in...as)
    CASE = auto()
    DEFAULT = auto()
    WHEN = auto()

    # Reactive programming tokens
    REACTIVE = auto()
    WATCH = auto()
    COMPUTED = auto()

    # Pipeline and composition tokens
    PIPELINE = auto()  # |> operator
    COMPOSE = auto()   # >> operator

    # Causal-Semantic tokens (نظام السببية والدلالة)
    CAUSE_EFFECT = auto()  # سبب_نتيجة
    RELATION = auto()  # علاقة
    CONDITION = auto()  # الشرط
    EFFECT_RESULT = auto()  # النتيجة
    CAUSE = auto()  # السبب
    IF_CONDITION = auto()  # إذا
    THEN_RESULT = auto()  # فإن

    # Cognitive-Semantic Model tokens
    COGNITIVE_ENTITY = auto()
    COGNITIVE_EVENT = auto()
    EVENT = auto()  # Generic event keyword
    TRIGGER = auto()
    CONCURRENT = auto()
    PATTERN = auto()
    CONCEPTUAL_BLUEPRINT = auto()
    IDEA = auto()
    PARTICIPANTS = auto()
    STRENGTH = auto()
    TRANSFORM = auto()
    REACTIONS = auto()
    STRUCTURE = auto()
    EXPRESS = auto()
    ENTITIES = auto()
    RESULT = auto()
    STATE_CHANGES = auto()
    LINGUISTIC_FORMS = auto()
    DEGREE = auto()
    ROLE = auto()

    # Semantic Programming & Knowledge Management
    MEANING = auto()
    SEMANTIC_QUERY = auto()
    # QUERY already defined in logical tokens
    INFORMATION = auto()
    CONTENT = auto()
    CONTEXT = auto()
    TIME = auto()
    PLACE = auto()
    SOURCE = auto()
    CERTAINTY = auto()
    INFERENCE_RULE = auto()
    INFER_FROM = auto()
    CONTRADICTION = auto()
    BETWEEN = auto()
    RESOLVE = auto()
    EVOLVING_KNOWLEDGE = auto()
    KNOWLEDGE = auto()
    CURRENT_VALUE = auto()
    HISTORY = auto()
    FUTURE_PREDICTION = auto()
    ONTOLOGY = auto()
    ROOT = auto()
    TAXONOMY = auto()
    MEMORY = auto()
    STORE = auto()
    RETRIEVE = auto()
    SIMILARITY = auto()
    # CONCEPT already defined in hybrid tokens
    NARRATIVE = auto()
    CHARACTERS = auto()
    # EVENTS already defined in cognitive-semantic tokens
    GENERATE_NARRATIVE = auto()
    BASED_ON = auto()
    CURRENT_CONTEXT = auto()

    # Existential model tokens (النموذج الوجودي)
    DOMAIN = auto()
    BASIC_ENTITY = auto()
    ENVIRONMENT = auto()
    IN_DOMAIN = auto()
    OF_TYPE = auto()
    EXISTENTIAL_BEING = auto()
    DIMENSIONS = auto()
    SPATIAL = auto()
    # TEMPORAL already defined in temporal tokens
    DOMAIN_SPECIFIC = auto()
    INTRINSIC_PROPERTIES = auto()
    INHERITED_MEANINGS = auto()
    INTRINSIC_MEANINGS = auto()
    # RELATIONS already defined
    # ACTIONS already defined
    # STATES already defined
    LAWS = auto()
    DOMAIN_RELATION = auto()
    DOMAIN_ACTION = auto()
    METAPHORICAL_MEANING = auto()
    BUILT_ON = auto()
    APPLIES_TO = auto()
    # CONDITIONS already defined
    DOMAIN_LAW = auto()
    EXISTENTIAL_QUERY = auto()
    ABOUT = auto()
    # Spatial directions
    ABOVE = auto()
    BELOW = auto()
    RIGHT = auto()
    LEFT = auto()
    FRONT = auto()
    BACK = auto()
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()
    # Temporal relations
    BEFORE = auto()
    AFTER = auto()
    DURING = auto()
    NOW = auto()
    # Prepositions (IN, FROM, AT already defined; ON, TO are new)
    ON = auto()
    TO = auto()
    # Life meanings (for life domain library)
    EMERGENCE = auto()
    LIFE = auto()
    GROWTH = auto()
    DEATH = auto()
    DECAY = auto()
    LIVING = auto()
    EAT = auto()
    DRINK = auto()
    FOOD = auto()
    SATIETY = auto()
    HUNGER = auto()
    WORK = auto()
    PAIN = auto()
    EFFECT = auto()
    AFFECTED = auto()
    STRUGGLE = auto()
    GAIN = auto()
    LOSS = auto()
    INTERIOR = auto()
    FACE = auto()
    SHADOW = auto()
    # Relations
    LOVE = auto()
    AFFECTION = auto()
    AVERSION = auto()
    PROXIMITY = auto()
    COOPERATION = auto()
    INTERACTION = auto()
    PRODUCT = auto()
    LAUGH = auto()
    CRY = auto()
    SPEAK = auto()
    THINK = auto()
    INHABITS = auto()
    MOVES_TO = auto()
    AFFECTED_BY = auto()

    # Special
    NEWLINE = auto()
    WHITESPACE = auto()
    COMMENT = auto()
    TILDE = auto()
    EOF = auto()

class Token:
    """Represents a token"""
    def __init__(self, type_, value, line, column):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, {self.line}:{self.column})"

class HybridLexer:
    """Hybrid lexer for Bayan language"""

    KEYWORDS = {
        'def': TokenType.DEF,
        'class': TokenType.CLASS,
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'elif': TokenType.ELIF,
        'for': TokenType.FOR,
        'while': TokenType.WHILE,
        'in': TokenType.IN,
        'print': TokenType.PRINT,
        'return': TokenType.RETURN,
        'yield': TokenType.YIELD,
        'break': TokenType.BREAK,
        'continue': TokenType.CONTINUE,
        'pass': TokenType.PASS,
        'True': TokenType.TRUE,
        'False': TokenType.FALSE,
        'None': TokenType.NONE,
        'and': TokenType.AND,
        'or': TokenType.OR,
        'not': TokenType.NOT,
        # Hybrid logic block (bilingual)
        'hybrid': TokenType.HYBRID,
        'هجين': TokenType.HYBRID,
        # Logical fact and rule (bilingual)
        'query': TokenType.QUERY,
        'fact': TokenType.FACT,
        'حقيقة': TokenType.FACT,
        'rule': TokenType.RULE,
        'قاعدة': TokenType.RULE,
        'self': TokenType.SELF,
        'super': TokenType.SUPER,
        'import': TokenType.IMPORT,
        'from': TokenType.FROM,
        'as': TokenType.AS,
        'try': TokenType.TRY,
        'except': TokenType.EXCEPT,
        'finally': TokenType.FINALLY,
        'raise': TokenType.RAISE,
        'is': TokenType.IS,
        'async': TokenType.ASYNC,
        'await': TokenType.AWAIT,
        'with': TokenType.WITH,
        # Entity/Action keywords (bilingual)
        'entity': TokenType.ENTITY,
        'كيان': TokenType.ENTITY,
        'apply': TokenType.APPLY,
        'طبق': TokenType.APPLY,
        'concept': TokenType.CONCEPT,
        'مفهوم': TokenType.CONCEPT,
        'once': TokenType.ONCE,
        'مرة': TokenType.ONCE,
        'limit': TokenType.LIMIT,
        'حد': TokenType.LIMIT,
        'match': TokenType.MATCH,
        'طابق': TokenType.MATCH,
        # Temporal keywords (bilingual)
        'temporal': TokenType.TEMPORAL,
        'زمنيا': TokenType.TEMPORAL,
        'زمني': TokenType.TEMPORAL,
        'within': TokenType.WITHIN,
        'خلال': TokenType.WITHIN,
        'schedule': TokenType.SCHEDULE,
        'جدول': TokenType.SCHEDULE,
        'جدولة': TokenType.SCHEDULE,
        'delay': TokenType.DELAY,
        'تأخير': TokenType.DELAY,
        'أخر': TokenType.DELAY,
        'every': TokenType.EVERY,
        'كل': TokenType.EVERY,
        'seconds': TokenType.SECONDS,
        'ثانية': TokenType.SECONDS,
        'ثواني': TokenType.SECONDS,
        'minutes': TokenType.MINUTES,
        'دقيقة': TokenType.MINUTES,
        'دقائق': TokenType.MINUTES,
        'hours': TokenType.HOURS,
        'ساعة': TokenType.HOURS,
        'ساعات': TokenType.HOURS,
        'first': TokenType.FIRST,
        'أولا': TokenType.FIRST,
        'أولاً': TokenType.FIRST,
        'then': TokenType.THEN,
        'ثم': TokenType.THEN,
        'lastly': TokenType.LASTLY,
        'أخيرا': TokenType.LASTLY,
        'أخيراً': TokenType.LASTLY,
        # Constraint keywords
        'where': TokenType.WHERE,
        'حيث': TokenType.WHERE,
        'requires': TokenType.REQUIRES,
        'يتطلب': TokenType.REQUIRES,
        'يشترط': TokenType.REQUIRES,
        'ensures': TokenType.ENSURES,
        'يضمن': TokenType.ENSURES,
        'يكفل': TokenType.ENSURES,
        'invariant': TokenType.INVARIANT,
        'ثابت': TokenType.INVARIANT,
        'ثوابت': TokenType.INVARIANT,
        # Pattern matching keywords
        'match': TokenType.MATCH,
        'طابق': TokenType.MATCH,
        'case': TokenType.CASE,
        'حالة': TokenType.CASE,
        'default': TokenType.DEFAULT,
        'افتراضي': TokenType.DEFAULT,
        'افتراضية': TokenType.DEFAULT,
        'when': TokenType.WHEN,
        'عندما': TokenType.WHEN,
        # Reactive programming keywords
        'reactive': TokenType.REACTIVE,
        'تفاعلي': TokenType.REACTIVE,
        'تفاعلية': TokenType.REACTIVE,
        'watch': TokenType.WATCH,
        'راقب': TokenType.WATCH,
        'مراقبة': TokenType.WATCH,
        'computed': TokenType.COMPUTED,
        'محسوب': TokenType.COMPUTED,
        'محسوبة': TokenType.COMPUTED,
        # Cognitive-Semantic Model keywords
        'cognitive_entity': TokenType.COGNITIVE_ENTITY,
        'كيان_معرفي': TokenType.COGNITIVE_ENTITY,
        'cognitive_event': TokenType.COGNITIVE_EVENT,
        'حدث_معرفي': TokenType.COGNITIVE_EVENT,
        'event': TokenType.EVENT,
        'حدث': TokenType.EVENT,
        'trigger': TokenType.TRIGGER,
        'أطلق': TokenType.TRIGGER,
        'concurrent': TokenType.CONCURRENT,
        'متزامن': TokenType.CONCURRENT,
        'pattern': TokenType.PATTERN,
        'قالب': TokenType.PATTERN,
        'conceptual_blueprint': TokenType.CONCEPTUAL_BLUEPRINT,
        'تصور_عام': TokenType.CONCEPTUAL_BLUEPRINT,
        'idea': TokenType.IDEA,
        'فكرة': TokenType.IDEA,
        'participants': TokenType.PARTICIPANTS,
        'مشاركون': TokenType.PARTICIPANTS,
        'strength': TokenType.STRENGTH,
        'قوة': TokenType.STRENGTH,
        'transform': TokenType.TRANSFORM,
        'تحويل': TokenType.TRANSFORM,
        'reactions': TokenType.REACTIONS,
        'ردود_فعل': TokenType.REACTIONS,
        'ردود': TokenType.REACTIONS,
        'structure': TokenType.STRUCTURE,
        'بنية': TokenType.STRUCTURE,
        'express': TokenType.EXPRESS,
        'تعبير': TokenType.EXPRESS,
        'entities': TokenType.ENTITIES,
        'كيانات': TokenType.ENTITIES,
        'result': TokenType.RESULT,
        'نتيجة': TokenType.RESULT,
        'state_changes': TokenType.STATE_CHANGES,
        'تغييرات_الحالة': TokenType.STATE_CHANGES,
        'تغييرات': TokenType.STATE_CHANGES,
        'linguistic_forms': TokenType.LINGUISTIC_FORMS,
        'أشكال_لغوية': TokenType.LINGUISTIC_FORMS,
        'أشكال': TokenType.LINGUISTIC_FORMS,
        'degree': TokenType.DEGREE,
        'درجة': TokenType.DEGREE,
        'role': TokenType.ROLE,
        'دور': TokenType.ROLE,
        # Semantic Programming & Knowledge Management keywords
        'meaning': TokenType.MEANING,
        'معنى': TokenType.MEANING,
        'semantic_query': TokenType.SEMANTIC_QUERY,
        'query': TokenType.QUERY,
        'استعلام': TokenType.QUERY,
        'information': TokenType.INFORMATION,
        'معلومة': TokenType.INFORMATION,
        # Causal-Semantic keywords (نظام السببية والدلالة)
        'سبب_نتيجة': TokenType.CAUSE_EFFECT,
        'cause_effect': TokenType.CAUSE_EFFECT,
        'علاقة': TokenType.RELATION,
        'relation': TokenType.RELATION,
        'الشرط': TokenType.CONDITION,
        'النتيجة': TokenType.EFFECT_RESULT,
        'السبب': TokenType.CAUSE,
        'إذا': TokenType.IF_CONDITION,
        'فإن': TokenType.THEN_RESULT,
        'القوة': TokenType.STRENGTH,
        'المجال': TokenType.DOMAIN,
        'content': TokenType.CONTENT,
        'محتوى': TokenType.CONTENT,
        'context': TokenType.CONTEXT,
        'سياق': TokenType.CONTEXT,
        'time': TokenType.TIME,
        'زمان': TokenType.TIME,
        'place': TokenType.PLACE,
        'مكان': TokenType.PLACE,
        'source': TokenType.SOURCE,
        'مصدر': TokenType.SOURCE,
        'certainty': TokenType.CERTAINTY,
        'يقين': TokenType.CERTAINTY,
        'inference_rule': TokenType.INFERENCE_RULE,
        'قاعدة_استدلال': TokenType.INFERENCE_RULE,
        'infer_from': TokenType.INFER_FROM,
        'استنتج': TokenType.INFER_FROM,
        'استنتج_من': TokenType.INFER_FROM,
        'contradiction': TokenType.CONTRADICTION,
        'تناقض': TokenType.CONTRADICTION,
        'between': TokenType.BETWEEN,
        'بين': TokenType.BETWEEN,
        'resolve': TokenType.RESOLVE,
        'حل': TokenType.RESOLVE,
        'evolving_knowledge': TokenType.EVOLVING_KNOWLEDGE,
        'knowledge': TokenType.KNOWLEDGE,
        'معرفة': TokenType.KNOWLEDGE,
        'current_value': TokenType.CURRENT_VALUE,
        'قيمة_حالية': TokenType.CURRENT_VALUE,
        'history': TokenType.HISTORY,
        'تاريخ': TokenType.HISTORY,
        'future_prediction': TokenType.FUTURE_PREDICTION,
        'توقع_مستقبلي': TokenType.FUTURE_PREDICTION,
        'ontology': TokenType.ONTOLOGY,
        'أنطولوجيا': TokenType.ONTOLOGY,
        'root': TokenType.ROOT,
        'جذر': TokenType.ROOT,
        'taxonomy': TokenType.TAXONOMY,
        'تصنيف': TokenType.TAXONOMY,
        'memory': TokenType.MEMORY,
        'ذاكرة': TokenType.MEMORY,
        'store': TokenType.STORE,
        'احفظ': TokenType.STORE,
        'retrieve': TokenType.RETRIEVE,
        'استرجع': TokenType.RETRIEVE,
        'similarity': TokenType.SIMILARITY,
        'تشابه': TokenType.SIMILARITY,
        # 'concept' and 'مفهوم' already defined in hybrid tokens
        'narrative': TokenType.NARRATIVE,
        'سرد': TokenType.NARRATIVE,
        'characters': TokenType.CHARACTERS,
        'شخصيات': TokenType.CHARACTERS,
        # 'events' and 'أحداث' already defined in cognitive-semantic tokens
        'generate_narrative': TokenType.GENERATE_NARRATIVE,
        'ولّد_سرد': TokenType.GENERATE_NARRATIVE,
        'based_on': TokenType.BASED_ON,
        'بناءً_على': TokenType.BASED_ON,
        'current_context': TokenType.CURRENT_CONTEXT,
        'سياق_حالي': TokenType.CURRENT_CONTEXT,

        # Existential model keywords (النموذج الوجودي)
        'domain': TokenType.DOMAIN,
        'مجال': TokenType.DOMAIN,
        'basic_entity': TokenType.BASIC_ENTITY,
        'كائن_أساسي': TokenType.BASIC_ENTITY,
        'environment': TokenType.ENVIRONMENT,
        'بيئة': TokenType.ENVIRONMENT,
        'in_domain': TokenType.IN_DOMAIN,
        'في_مجال': TokenType.IN_DOMAIN,
        'of_type': TokenType.OF_TYPE,
        'من_نوع': TokenType.OF_TYPE,
        'existential_being': TokenType.EXISTENTIAL_BEING,
        'كائن_وجودي': TokenType.EXISTENTIAL_BEING,
        'dimensions': TokenType.DIMENSIONS,
        'أبعاد': TokenType.DIMENSIONS,
        'spatial': TokenType.SPATIAL,
        'مكاني': TokenType.SPATIAL,
        'temporal': TokenType.TEMPORAL,
        'زماني': TokenType.TEMPORAL,
        'domain_specific': TokenType.DOMAIN_SPECIFIC,
        'مجالي': TokenType.DOMAIN_SPECIFIC,
        'intrinsic_properties': TokenType.INTRINSIC_PROPERTIES,
        'خصائص_ذاتية': TokenType.INTRINSIC_PROPERTIES,
        'inherited_meanings': TokenType.INHERITED_MEANINGS,
        'معانٍ_موروثة': TokenType.INHERITED_MEANINGS,
        'معاني_موروثة': TokenType.INHERITED_MEANINGS,
        'intrinsic_meanings': TokenType.INTRINSIC_MEANINGS,
        'معانٍ_ذاتية': TokenType.INTRINSIC_MEANINGS,
        'معاني_ذاتية': TokenType.INTRINSIC_MEANINGS,
        'laws': TokenType.LAWS,
        'قوانين': TokenType.LAWS,
        'domain_relation': TokenType.DOMAIN_RELATION,
        'علاقة_مجالية': TokenType.DOMAIN_RELATION,
        'domain_action': TokenType.DOMAIN_ACTION,
        'فعل_مجالي': TokenType.DOMAIN_ACTION,
        'metaphorical_meaning': TokenType.METAPHORICAL_MEANING,
        'معنى_مجازي': TokenType.METAPHORICAL_MEANING,
        'built_on': TokenType.BUILT_ON,
        'يُبنى_على': TokenType.BUILT_ON,
        'يبنى_على': TokenType.BUILT_ON,
        'applies_to': TokenType.APPLIES_TO,
        'يُطبق_على': TokenType.APPLIES_TO,
        'يطبق_على': TokenType.APPLIES_TO,
        'domain_law': TokenType.DOMAIN_LAW,
        'قانون_مجالي': TokenType.DOMAIN_LAW,
        'existential_query': TokenType.EXISTENTIAL_QUERY,
        'استعلام_وجودي': TokenType.EXISTENTIAL_QUERY,
        'about': TokenType.ABOUT,
        'عن': TokenType.ABOUT,

        # Spatial directions (الاتجاهات المكانية)
        'above': TokenType.ABOVE,
        'فوق': TokenType.ABOVE,
        'below': TokenType.BELOW,
        'تحت': TokenType.BELOW,
        'right': TokenType.RIGHT,
        'يمين': TokenType.RIGHT,
        'left': TokenType.LEFT,
        'يسار': TokenType.LEFT,
        'front': TokenType.FRONT,
        'أمام': TokenType.FRONT,
        'back': TokenType.BACK,
        'خلف': TokenType.BACK,
        'north': TokenType.NORTH,
        'شمال': TokenType.NORTH,
        'south': TokenType.SOUTH,
        'جنوب': TokenType.SOUTH,
        'east': TokenType.EAST,
        'شرق': TokenType.EAST,
        'west': TokenType.WEST,
        'غرب': TokenType.WEST,

        # Temporal relations (العلاقات الزمانية)
        'before': TokenType.BEFORE,
        'قبل': TokenType.BEFORE,
        'after': TokenType.AFTER,
        'بعد': TokenType.AFTER,
        'during': TokenType.DURING,
        'أثناء': TokenType.DURING,
        'now': TokenType.NOW,
        'الآن': TokenType.NOW,

        # Prepositions (حروف الجر)
        'in': TokenType.IN,
        'في': TokenType.IN,
        'on': TokenType.ON,
        'على': TokenType.ON,
        'to': TokenType.TO,
        'إلى': TokenType.TO,
        'from': TokenType.FROM,
        'من': TokenType.FROM,
        'at': TokenType.AT,
        'عند': TokenType.AT,

        # Life meanings (المعاني الحياتية - for life domain library)
        'emergence': TokenType.EMERGENCE,
        'انبثاق': TokenType.EMERGENCE,
        'life': TokenType.LIFE,
        'حياة': TokenType.LIFE,
        'growth': TokenType.GROWTH,
        'نمو': TokenType.GROWTH,
        'death': TokenType.DEATH,
        'موت': TokenType.DEATH,
        'decay': TokenType.DECAY,
        'اضمحلال': TokenType.DECAY,
        'living': TokenType.LIVING,
        'عيش': TokenType.LIVING,
        'eat': TokenType.EAT,
        'أكل': TokenType.EAT,
        'drink': TokenType.DRINK,
        'شرب': TokenType.DRINK,
        'food': TokenType.FOOD,
        'طعام': TokenType.FOOD,
        'satiety': TokenType.SATIETY,
        'شبع': TokenType.SATIETY,
        'hunger': TokenType.HUNGER,
        'جوع': TokenType.HUNGER,
        'work': TokenType.WORK,
        'عمل': TokenType.WORK,
        'pain': TokenType.PAIN,
        'ألم': TokenType.PAIN,
        'effect': TokenType.EFFECT,
        'أثر': TokenType.EFFECT,
        'affected': TokenType.AFFECTED,
        'تأثر': TokenType.AFFECTED,
        'struggle': TokenType.STRUGGLE,
        'صراع': TokenType.STRUGGLE,
        'gain': TokenType.GAIN,
        'كسب': TokenType.GAIN,
        'loss': TokenType.LOSS,
        'فقدان': TokenType.LOSS,
        'interior': TokenType.INTERIOR,
        'جوف': TokenType.INTERIOR,
        'face': TokenType.FACE,
        'وجه': TokenType.FACE,
        'shadow': TokenType.SHADOW,
        'ظل': TokenType.SHADOW,

        # Relations (العلاقات)
        'love': TokenType.LOVE,
        'حب': TokenType.LOVE,
        'affection': TokenType.AFFECTION,
        'ود': TokenType.AFFECTION,
        'aversion': TokenType.AVERSION,
        'نفور': TokenType.AVERSION,
        'proximity': TokenType.PROXIMITY,
        'تقارب': TokenType.PROXIMITY,
        'cooperation': TokenType.COOPERATION,
        'تعاون': TokenType.COOPERATION,
        'interaction': TokenType.INTERACTION,
        'تفاعل': TokenType.INTERACTION,
        'product': TokenType.PRODUCT,
        'نتاج': TokenType.PRODUCT,
        'laugh': TokenType.LAUGH,
        'ضحك': TokenType.LAUGH,
        'cry': TokenType.CRY,
        'بكاء': TokenType.CRY,
        'speak': TokenType.SPEAK,
        'تكلم': TokenType.SPEAK,
        'think': TokenType.THINK,
        'تفكر': TokenType.THINK,
        'inhabits': TokenType.INHABITS,
        'يسكن_في': TokenType.INHABITS,
        'moves_to': TokenType.MOVES_TO,
        'يتحرك_إلى': TokenType.MOVES_TO,
        'affected_by': TokenType.AFFECTED_BY,
        'يتأثر_بـ': TokenType.AFFECTED_BY,
        'يتأثر_ب': TokenType.AFFECTED_BY,
    }

    def __init__(self, code):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    def tokenize(self):
        """Tokenize the code"""
        while self.position < len(self.code):
            self._skip_whitespace_and_comments()

            if self.position >= len(self.code):
                break

            if not self._match_token():
                char = self.code[self.position]
                raise SyntaxError(f"Unknown character '{char}' at {self.line}:{self.column}")

        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens

    def _skip_whitespace_and_comments(self):
        """Skip whitespace and comments"""
        while self.position < len(self.code):
            # Skip whitespace
            if self.code[self.position] in ' \t\r':
                self.position += 1
                self.column += 1
            # Handle newlines
            elif self.code[self.position] == '\n':
                self.position += 1
                self.line += 1
                self.column = 1
            # Handle comments
            elif self.code[self.position] == '#':
                while self.position < len(self.code) and self.code[self.position] != '\n':
                    self.position += 1
            else:
                break


    def _match_triple_string(self):
        """Match a triple-quoted string supporting newlines."""
        if self.code.startswith('"""', self.position):
            quote = '"""'
        elif self.code.startswith("'''", self.position):
            quote = "'''"
        else:
            return False
        start_pos = self.position
        start_line = self.line
        start_col = self.column
        # Advance past opening quote
        self.position += 3
        self.column += 3
        while self.position < len(self.code):
            if self.code.startswith(quote, self.position):
                # Include closing quotes
                self.position += 3
                self.column += 3
                lexeme = self.code[start_pos:self.position]
                self.tokens.append(Token(TokenType.STRING, lexeme, start_line, start_col))
                return True
            ch = self.code[self.position]
            if ch == '\n':
                self.position += 1
                self.line += 1
                self.column = 1
            else:
                self.position += 1
                self.column += 1
        raise SyntaxError(f"Unterminated triple-quoted string at {start_line}:{start_col}")

    def _match_token(self):
        """Try to match a token at current position"""
        # Query operator (?-)
        if self._match_pattern(r'\?-', TokenType.QUERY):
            return True

        # Logical variable (?X, ?name)
        if self._match_pattern(r'\?[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*', TokenType.VARIABLE):
            return True

        # Strings (triple-quoted first)
        if self._match_triple_string():
            return True
        if self._match_pattern(r'"[^"]*"', TokenType.STRING) or self._match_pattern(r"'[^']*'", TokenType.STRING):
            return True

        # Numbers
        if self._match_pattern(r'\d+(\.\d+)?', TokenType.NUMBER):
            return True

        # Identifiers and keywords
        if self._match_pattern(r'[a-zA-Z_\u0600-\u06FF][a-zA-Z0-9_\u0600-\u06FF]*'):
            return True

        # Operators and symbols
        if self._match_pattern(r'←|:-', TokenType.IMPLIES):
            return True
        # Membership symbol ∈
        if self._match_pattern(r'∈', TokenType.IN):
            return True
        # Pipeline and composition operators (before other operators)
        if self._match_pattern(r'\|>', TokenType.PIPELINE):
            return True
        if self._match_pattern(r'>>', TokenType.COMPOSE):
            return True
        # Approximate equality operators first to avoid splitting '~='
        if self._match_pattern(r'~=|≈', TokenType.OPERATOR):
            return True
        if self._match_pattern(r'==|!=|<=|>=|<|>', TokenType.OPERATOR):
            return True
        # Match ** before * to avoid splitting it
        if self._match_pattern(r'\*\*', TokenType.OPERATOR):
            return True
        if self._match_pattern(r'[+\-*/%]', TokenType.OPERATOR):
            return True
        if self._match_pattern(r'=', TokenType.ASSIGN):
            return True
        # Tilde alone (sampling)
        if self._match_pattern(r'~', TokenType.TILDE):
            return True
        if self._match_pattern(r'\.', TokenType.DOT):
            return True
        if self._match_pattern(r',', TokenType.COMMA):
            return True
        if self._match_pattern(r';', TokenType.SEMICOLON):
            return True
        if self._match_pattern(r':', TokenType.COLON):
            return True
        if self._match_pattern(r'\(', TokenType.LPAREN):
            return True
        if self._match_pattern(r'\)', TokenType.RPAREN):
            return True
        if self._match_pattern(r'\{', TokenType.LBRACE):
            return True
        if self._match_pattern(r'\}', TokenType.RBRACE):
            return True
        if self._match_pattern(r'\[', TokenType.LBRACKET):
            return True
        if self._match_pattern(r'\]', TokenType.RBRACKET):
            return True
        if self._match_pattern(r'->', TokenType.ARROW):
            return True
        if self._match_pattern(r'\|', TokenType.PIPE):
            return True
        if self._match_pattern(r'@', TokenType.AT):
            return True
        if self._match_pattern(r'!', TokenType.CUT):
            return True

        return False

    def _match_pattern(self, pattern, token_type=None):
        """Try to match a regex pattern"""
        regex = re.compile(pattern)
        match = regex.match(self.code, self.position)

        if match:
            value = match.group(0)
            self.position = match.end()

            # Determine token type if not provided
            if token_type is None:
                if value.startswith('?'):
                    token_type = TokenType.VARIABLE
                elif value in self.KEYWORDS:
                    token_type = self.KEYWORDS[value]
                elif value[0] in '"\'':
                    token_type = TokenType.STRING
                elif value[0].isdigit():
                    token_type = TokenType.NUMBER
                else:
                    token_type = TokenType.IDENTIFIER

            self._add_token(token_type, value)
            self.column += len(value)
            return True

        return False

    def _add_token(self, token_type, value=None):
        """Add a token to the list"""
        if value is None:
            value = self.code[self.position:self.position + 1]

        token = Token(token_type, value, self.line, self.column)
        self.tokens.append(token)

