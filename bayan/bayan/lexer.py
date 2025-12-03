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
    FSTRING = auto()  # f-string (formatted string literal)
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
    QUESTION = auto()  # Query terminator (?)

    # Async tokens
    ASYNC = auto()
    AWAIT = auto()

    # Lambda token
    LAMBDA = auto()

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

    # Scope keywords
    GLOBAL = auto()
    NONLOCAL = auto()

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
    SEMANTIC_NETWORK = auto()
    INFER_FROM_TEXT = auto()
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

    # Type System tokens (نظام الأنواع)
    TYPE_INT = auto()       # int / صحيح
    TYPE_FLOAT = auto()     # float / عشري
    TYPE_STR = auto()       # str / نص
    TYPE_BOOL = auto()      # bool / منطقي
    TYPE_LIST = auto()      # list / قائمة
    TYPE_DICT = auto()      # dict / قاموس
    TYPE_SET = auto()       # set / مجموعة
    TYPE_TUPLE = auto()     # tuple / صف
    TYPE_OPTIONAL = auto()  # Optional / اختياري
    TYPE_UNION = auto()     # Union / اتحاد
    TYPE_ANY = auto()       # Any / أي
    TYPE_NONE = auto()      # None / لاشيء (as type)
    TYPE_CALLABLE = auto()  # Callable / قابل_للاستدعاء
    TYPE_SELF = auto()      # Self / ذاتي (for return type)
    ENUM = auto()           # enum / تعداد
    INTERFACE = auto()      # interface / واجهة
    IMPLEMENTS = auto()     # implements / ينفذ
    EXTENDS = auto()        # extends / يرث
    ABSTRACT = auto()       # abstract / مجرد
    OVERRIDE = auto()       # override / تجاوز
    FINAL = auto()          # final / نهائي
    CONST = auto()          # const / ثابت
    STATIC = auto()         # static / ساكن
    PRIVATE = auto()        # private / خاص
    PUBLIC = auto()         # public / عام
    PROTECTED = auto()      # protected / محمي
    READONLY = auto()       # readonly / للقراءة_فقط

    # Additional language features
    ASSERT = auto()         # assert / تأكد
    QUESTION_DOT = auto()   # ?. Optional chaining
    NULLISH = auto()        # ?? Null coalescing
    STAR_STAR = auto()      # ** for dict unpacking
    WALRUS = auto()         # := assignment expression

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
        # Function definition (تعريف الدالة)
        'def': TokenType.DEF,
        'دالة': TokenType.DEF,
        'عرف': TokenType.DEF,
        # Class definition (تعريف الصنف)
        'class': TokenType.CLASS,
        'صنف': TokenType.CLASS,
        'فئة': TokenType.CLASS,
        # Control flow (التحكم في التدفق)
        'if': TokenType.IF,
        'إذا': TokenType.IF,
        'لو': TokenType.IF,
        'else': TokenType.ELSE,
        'وإلا': TokenType.ELSE,
        'غير_ذلك': TokenType.ELSE,
        'elif': TokenType.ELIF,
        'وإلا_إذا': TokenType.ELIF,
        'أو_إذا': TokenType.ELIF,
        # Loops (الحلقات)
        'for': TokenType.FOR,
        'لكل': TokenType.FOR,
        'كرر': TokenType.FOR,
        'while': TokenType.WHILE,
        'طالما': TokenType.WHILE,
        'بينما': TokenType.WHILE,
        'in': TokenType.IN,
        # I/O (الإدخال والإخراج)
        'print': TokenType.PRINT,
        'اطبع': TokenType.PRINT,
        # Function control (التحكم في الدوال)
        'return': TokenType.RETURN,
        'أرجع': TokenType.RETURN,
        'ارجع': TokenType.RETURN,
        'yield': TokenType.YIELD,
        'أنتج': TokenType.YIELD,
        'انتج': TokenType.YIELD,
        # Loop control (التحكم في الحلقات)
        'break': TokenType.BREAK,
        'اكسر': TokenType.BREAK,
        'توقف': TokenType.BREAK,
        'continue': TokenType.CONTINUE,
        'استمر': TokenType.CONTINUE,
        'تابع': TokenType.CONTINUE,
        'pass': TokenType.PASS,
        'مرر': TokenType.PASS,
        'تجاوز': TokenType.PASS,
        # Boolean values (القيم المنطقية)
        'True': TokenType.TRUE,
        'صحيح': TokenType.TRUE,
        'صح': TokenType.TRUE,
        'False': TokenType.FALSE,
        'خطأ': TokenType.FALSE,
        'خاطئ': TokenType.FALSE,
        'None': TokenType.NONE,
        'لاشيء': TokenType.NONE,
        'فارغ': TokenType.NONE,
        'عدم': TokenType.NONE,
        # Logical operators (العوامل المنطقية)
        'and': TokenType.AND,
        'و': TokenType.AND,
        'or': TokenType.OR,
        'أو': TokenType.OR,
        'not': TokenType.NOT,
        'ليس': TokenType.NOT,
        'لا': TokenType.NOT,
        # Hybrid logic block (bilingual)
        'hybrid': TokenType.HYBRID,
        'هجين': TokenType.HYBRID,
        # Logical fact and rule (bilingual)
        'query': TokenType.QUERY,
        'fact': TokenType.FACT,
        'حقيقة': TokenType.FACT,
        'rule': TokenType.RULE,
        'قاعدة': TokenType.RULE,
        # Object-oriented (البرمجة الكائنية)
        'self': TokenType.SELF,
        'ذاتي': TokenType.SELF,
        'نفسي': TokenType.SELF,
        'super': TokenType.SUPER,
        'أب': TokenType.SUPER,
        'الأب': TokenType.SUPER,
        # Import/Export (الاستيراد والتصدير)
        'import': TokenType.IMPORT,
        'استورد': TokenType.IMPORT,
        'from': TokenType.FROM,
        'من': TokenType.FROM,
        'as': TokenType.AS,
        'كـ': TokenType.AS,
        # Exception handling (معالجة الاستثناءات)
        'try': TokenType.TRY,
        'حاول': TokenType.TRY,
        'جرب': TokenType.TRY,
        'except': TokenType.EXCEPT,
        'استثنِ': TokenType.EXCEPT,
        'استثن': TokenType.EXCEPT,
        'عدا': TokenType.EXCEPT,
        'finally': TokenType.FINALLY,
        'أخيراً': TokenType.FINALLY,
        'في_النهاية': TokenType.FINALLY,
        'raise': TokenType.RAISE,
        'أطلق_خطأ': TokenType.RAISE,
        'ارفع': TokenType.RAISE,
        # Identity operator (عامل الهوية)
        'is': TokenType.IS,
        'هو': TokenType.IS,
        'يكون': TokenType.IS,
        # Async/Await (البرمجة غير المتزامنة)
        'async': TokenType.ASYNC,
        'غير_متزامن': TokenType.ASYNC,
        'متزامن_لا': TokenType.ASYNC,
        'await': TokenType.AWAIT,
        'انتظر': TokenType.AWAIT,
        # Context manager (مدير السياق)
        'with': TokenType.WITH,
        'مع': TokenType.WITH,
        'باستخدام': TokenType.WITH,
        # Lambda (تعبير الدالة)
        'lambda': TokenType.LAMBDA,
        'تعبير_دالة': TokenType.LAMBDA,
        'دالة_مختصرة': TokenType.LAMBDA,
        # Scope (نطاق المتغيرات)
        'global': TokenType.GLOBAL,
        'عام': TokenType.GLOBAL,
        'عمومي': TokenType.GLOBAL,
        'nonlocal': TokenType.NONLOCAL,
        'محلي_خارجي': TokenType.NONLOCAL,
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
        'ختاماً': TokenType.LASTLY,
        'في_الختام': TokenType.LASTLY,
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
        # 'match' and 'طابق' already defined above
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
        'semantic_network': TokenType.SEMANTIC_NETWORK,
        'شبكة_معاني': TokenType.SEMANTIC_NETWORK,
        'استدل_من': TokenType.INFER_FROM_TEXT,
        'infer_from_text': TokenType.INFER_FROM_TEXT,
        # 'query' already defined above
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
        'إذا_شرط': TokenType.IF_CONDITION,
        'شرط_إذا': TokenType.IF_CONDITION,
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
        'infer': TokenType.INFER_FROM,
        'استنتج': TokenType.INFER_FROM,
        'استنتج_من': TokenType.INFER_FROM,
        'contradiction': TokenType.CONTRADICTION,
        'تناقض': TokenType.CONTRADICTION,
        'between': TokenType.BETWEEN,
        'بين': TokenType.BETWEEN,
        'resolve': TokenType.RESOLVE,
        'حل': TokenType.RESOLVE,
        'evolving_knowledge': TokenType.EVOLVING_KNOWLEDGE,
        'معرفة_متطورة': TokenType.EVOLVING_KNOWLEDGE,
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
        'semantic_memory': TokenType.MEMORY,
        'ذاكرة_دلالية': TokenType.MEMORY,
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
        # 'temporal' already defined above
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
        # 'in' already defined above for loops
        'في': TokenType.IN,
        'on': TokenType.ON,
        'على': TokenType.ON,
        'to': TokenType.TO,
        'إلى': TokenType.TO,
        # 'from' and 'من' already defined above for imports
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

        # Type System keywords (كلمات نظام الأنواع)
        'int': TokenType.TYPE_INT,
        'عدد_صحيح': TokenType.TYPE_INT,
        'نوع_صحيح': TokenType.TYPE_INT,
        'float': TokenType.TYPE_FLOAT,
        'عشري': TokenType.TYPE_FLOAT,
        'عدد_عشري': TokenType.TYPE_FLOAT,
        'str': TokenType.TYPE_STR,
        'نص': TokenType.TYPE_STR,
        'سلسلة': TokenType.TYPE_STR,
        'bool': TokenType.TYPE_BOOL,
        'منطقي': TokenType.TYPE_BOOL,
        'list': TokenType.TYPE_LIST,
        'قائمة': TokenType.TYPE_LIST,
        'dict': TokenType.TYPE_DICT,
        'قاموس': TokenType.TYPE_DICT,
        'set': TokenType.TYPE_SET,
        'مجموعة_نوع': TokenType.TYPE_SET,
        'tuple': TokenType.TYPE_TUPLE,
        'صف': TokenType.TYPE_TUPLE,
        'Optional': TokenType.TYPE_OPTIONAL,
        'اختياري': TokenType.TYPE_OPTIONAL,
        'Union': TokenType.TYPE_UNION,
        'اتحاد': TokenType.TYPE_UNION,
        'Any': TokenType.TYPE_ANY,
        'أي': TokenType.TYPE_ANY,
        'Callable': TokenType.TYPE_CALLABLE,
        'قابل_للاستدعاء': TokenType.TYPE_CALLABLE,
        'Self': TokenType.TYPE_SELF,
        'ذاتي_نوع': TokenType.TYPE_SELF,
        'enum': TokenType.ENUM,
        'تعداد': TokenType.ENUM,
        'interface': TokenType.INTERFACE,
        'واجهة': TokenType.INTERFACE,
        'implements': TokenType.IMPLEMENTS,
        'ينفذ': TokenType.IMPLEMENTS,
        'يطبق': TokenType.IMPLEMENTS,
        'abstract': TokenType.ABSTRACT,
        'مجرد': TokenType.ABSTRACT,
        'override': TokenType.OVERRIDE,
        'تخطي': TokenType.OVERRIDE,
        'استبدال': TokenType.OVERRIDE,
        'final': TokenType.FINAL,
        'نهائي': TokenType.FINAL,
        'const': TokenType.CONST,
        'ثابت_قيمة': TokenType.CONST,
        'قيمة_ثابتة': TokenType.CONST,
        'static': TokenType.STATIC,
        'staticmethod': TokenType.STATIC,
        'ساكن': TokenType.STATIC,
        'private': TokenType.PRIVATE,
        'خاص': TokenType.PRIVATE,
        'public': TokenType.PUBLIC,
        'علني': TokenType.PUBLIC,
        'عامة': TokenType.PUBLIC,
        'protected': TokenType.PROTECTED,
        'محمي': TokenType.PROTECTED,
        'readonly': TokenType.READONLY,
        'للقراءة_فقط': TokenType.READONLY,
        'extends': TokenType.EXTENDS,
        'يرث': TokenType.EXTENDS,
        'يمتد': TokenType.EXTENDS,
        # Assert keyword
        'assert': TokenType.ASSERT,
        'تأكد': TokenType.ASSERT,
        'أكد': TokenType.ASSERT,
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
            # Handle single-line comments (# or //)
            elif self.code[self.position] == '#':
                while self.position < len(self.code) and self.code[self.position] != '\n':
                    self.position += 1
            elif self.code[self.position:self.position + 2] == '//':
                while self.position < len(self.code) and self.code[self.position] != '\n':
                    self.position += 1
            # Handle multi-line comments /* ... */
            elif self.code[self.position:self.position + 2] == '/*':
                self.position += 2
                self.column += 2
                while self.position < len(self.code) - 1:
                    if self.code[self.position:self.position + 2] == '*/':
                        self.position += 2
                        self.column += 2
                        break
                    elif self.code[self.position] == '\n':
                        self.position += 1
                        self.line += 1
                        self.column = 1
                    else:
                        self.position += 1
                        self.column += 1
            else:
                break


    def _match_fstring(self):
        """Match an f-string (formatted string literal).

        Supports: f"..." or f'...'
        """
        # Check for f" or f'
        if self.position + 1 >= len(self.code):
            return False

        if self.code[self.position] != 'f':
            return False

        next_char = self.code[self.position + 1]
        if next_char not in '"\'':
            return False

        start_pos = self.position
        start_line = self.line
        start_col = self.column
        quote = next_char

        # Skip 'f' and opening quote
        self.position += 2
        self.column += 2

        # Find closing quote (handle escaped quotes)
        while self.position < len(self.code):
            ch = self.code[self.position]
            if ch == '\\' and self.position + 1 < len(self.code):
                # Skip escaped character
                self.position += 2
                self.column += 2
            elif ch == quote:
                # Found closing quote
                self.position += 1
                self.column += 1
                lexeme = self.code[start_pos:self.position]
                self.tokens.append(Token(TokenType.FSTRING, lexeme, start_line, start_col))
                return True
            elif ch == '\n':
                raise SyntaxError(f"Unterminated f-string at {start_line}:{start_col}")
            else:
                self.position += 1
                self.column += 1

        raise SyntaxError(f"Unterminated f-string at {start_line}:{start_col}")

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

        # Strings (f-strings first, then triple-quoted, then regular)
        if self._match_fstring():
            return True
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
        # Arrow operator -> (must be before - operator to avoid splitting)
        if self._match_pattern(r'->', TokenType.ARROW):
            return True
        # Prolog-style negation as failure \+ (must be before other backslash operators)
        if self._match_pattern(r'\\[+]', TokenType.NOT):
            return True
        # Prolog-style not-equal \= (must be before other operators)
        if self._match_pattern(r'\\=', TokenType.OPERATOR):
            return True
        if self._match_pattern(r'==|!=|<=|>=|<|>', TokenType.OPERATOR):
            return True
        # Walrus operator := (assignment expression)
        if self._match_pattern(r':=', TokenType.WALRUS):
            return True
        # Nullish coalescing operator ??
        if self._match_pattern(r'\?\?', TokenType.NULLISH):
            return True
        # Optional chaining ?. (must be before DOT)
        if self._match_pattern(r'\?\.', TokenType.QUESTION_DOT):
            return True
        # Match ** before * to avoid splitting it
        if self._match_pattern(r'\*\*', TokenType.STAR_STAR):
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
        if self._match_pattern(r'\|', TokenType.PIPE):
            return True
        # Prolog-style term comparison operators @<, @>, @=<, @>=
        if self._match_pattern(r'@=<|@>=|@<|@>', TokenType.OPERATOR):
            return True
        if self._match_pattern(r'@', TokenType.AT):
            return True
        if self._match_pattern(r'!', TokenType.CUT):
            return True
        if self._match_pattern(r'\?', TokenType.QUESTION):
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

