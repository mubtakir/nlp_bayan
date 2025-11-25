"""
Built-in functions and utilities for Bayan Language
دوال مدمجة وأدوات للغة بيان
"""

from .logical_engine import Term, Predicate
from .gse import GSEModel, generalized_sigmoid
from .mother_equation import (
    MotherEquation, Property, State, PropertyDomain,
    create_example_human, create_example_tree, create_example_building
)
from .linguistic_equation import (
    LinguisticEquation, EntityState, Role, EventType,
    KnowledgeBase, LinguisticEquationParser,
    create_simple_equation
)

try:
    from .gse_fitting import GSEFitter
    GSE_FITTING_AVAILABLE = True
except ImportError:
    GSE_FITTING_AVAILABLE = False

class BuiltinFunctions:
    """Collection of built-in functions"""
    
    @staticmethod
    def member(element, lst):
        """Check if element is member of list"""
        return element in lst
    
    @staticmethod
    def append(lst, element):
        """Append element to list"""
        lst.append(element)
        return lst
    
    @staticmethod
    def length(lst):
        """Get length of list"""
        return len(lst)
    
    @staticmethod
    def reverse(lst):
        """Reverse a list"""
        return list(reversed(lst))
    
    @staticmethod
    def sort(lst):
        """Sort a list"""
        return sorted(lst)
    
    @staticmethod
    def max_val(lst):
        """Get maximum value from list"""
        return max(lst)
    
    @staticmethod
    def min_val(lst):
        """Get minimum value from list"""
        return min(lst)
    
    @staticmethod
    def sum_val(lst):
        """Sum all values in list"""
        return sum(lst)

    @staticmethod
    def isinstance_check(obj, type_or_tuple):
        """Check if object is instance of a type"""
        return isinstance(obj, type_or_tuple)

    @staticmethod
    def type_of(obj):
        """Get type of object"""
        return type(obj)

    @staticmethod
    def callable_check(obj):
        """Check if object is callable"""
        return callable(obj)

    @staticmethod
    def hasattr_check(obj, name):
        """Check if object has attribute"""
        return hasattr(obj, name)

    @staticmethod
    def getattr_val(obj, name, default=None):
        """Get attribute value from object"""
        return getattr(obj, name, default)

    @staticmethod
    def setattr_val(obj, name, value):
        """Set attribute value on object"""
        setattr(obj, name, value)
        return None
    
    @staticmethod
    def average(lst):
        """Calculate average of list"""
        return sum(lst) / len(lst) if lst else 0
    
    @staticmethod
    def abs_val(x):
        """Absolute value"""
        return abs(x)
    
    @staticmethod
    def power(x, y):
        """Power function"""
        return x ** y
    
    @staticmethod
    def sqrt(x):
        """Square root"""
        return x ** 0.5
    
    @staticmethod
    def round_val(x, decimals=0):
        """Round a number"""
        return round(x, decimals)
    
    @staticmethod
    def floor_val(x):
        """Floor function"""
        import math
        return math.floor(x)
    
    @staticmethod
    def ceil_val(x):
        """Ceiling function"""
        import math
        return math.ceil(x)
    
    @staticmethod
    def upper(s):
        """Convert string to uppercase"""
        return s.upper()
    
    @staticmethod
    def lower(s):
        """Convert string to lowercase"""
        return s.lower()
    
    @staticmethod
    def strip(s):
        """Strip whitespace from string"""
        return s.strip()
    
    @staticmethod
    def split(s, delimiter=' '):
        """Split string"""
        return s.split(delimiter)
    
    @staticmethod
    def join(lst, delimiter=''):
        """Join list into string"""
        return delimiter.join(str(x) for x in lst)
    
    @staticmethod
    def replace(s, old, new):
        """Replace substring"""
        return s.replace(old, new)
    
    @staticmethod
    def contains(s, substring):
        """Check if string contains substring"""
        return substring in s
    
    @staticmethod
    def starts_with(s, prefix):
        """Check if string starts with prefix"""
        return s.startswith(prefix)
    
    @staticmethod
    def ends_with(s, suffix):
        """Check if string ends with suffix"""
        return s.endswith(suffix)
    
    @staticmethod
    def find(s, substring):
        """Find index of substring"""
        return s.find(substring)
    
    @staticmethod
    def keys(d):
        """Get dictionary keys"""
        return list(d.keys())
    
    @staticmethod
    def values(d):
        """Get dictionary values"""
        return list(d.values())
    
    @staticmethod
    def items(d):
        """Get dictionary items"""
        return list(d.items())
    
    @staticmethod
    def get(d, key, default=None):
        """Get value from dictionary"""
        return d.get(key, default)
    
    @staticmethod
    def set_val(d, key, value):
        """Set value in dictionary"""
        d[key] = value
        return d
    
    @staticmethod
    def delete(d, key):
        """Delete key from dictionary"""
        if key in d:
            del d[key]
        return d
    
    @staticmethod
    def type_of(obj):
        """Get type of object"""
        return type(obj).__name__
    
    @staticmethod
    def is_number(obj):
        """Check if object is number"""
        return isinstance(obj, (int, float))
    
    @staticmethod
    def is_string(obj):
        """Check if object is string"""
        return isinstance(obj, str)
    
    @staticmethod
    def is_list(obj):
        """Check if object is list"""
        return isinstance(obj, list)
    
    @staticmethod
    def is_dict(obj):
        """Check if object is dictionary"""
        return isinstance(obj, dict)
    
    @staticmethod
    def is_boolean(obj):
        """Check if object is boolean"""
        return isinstance(obj, bool)

    @staticmethod
    def is_none(obj):
        """Check if object is None"""
        return obj is None

    @staticmethod
    def all_true(lst):
        """Check if all elements are truthy"""
        return all(lst)

    @staticmethod
    def any_true(lst):
        """Check if any element is truthy"""
        return any(lst)

    @staticmethod
    def enumerate_list(lst, start=0):
        """Enumerate a list"""
        return list(enumerate(lst, start))

    @staticmethod
    def zip_lists(*lists):
        """Zip multiple lists together"""
        return list(zip(*lists))

    @staticmethod
    def filter_list(predicate, lst):
        """Filter list by predicate"""
        return list(filter(predicate, lst))

    @staticmethod
    def map_list(func, lst):
        """Map function over list"""
        return list(map(func, lst))

    @staticmethod
    def reduce_list(func, lst, initial=None):
        """Reduce list with function"""
        from functools import reduce
        if initial is None:
            return reduce(func, lst)
        return reduce(func, lst, initial)

    @staticmethod
    def slice_list(lst, start=None, end=None, step=None):
        """Slice a list"""
        return lst[start:end:step]

    @staticmethod
    def index_of(lst, element):
        """Find index of element in list"""
        try:
            return lst.index(element)
        except ValueError:
            return -1

    @staticmethod
    def count_occurrences(lst, element):
        """Count occurrences of element in list"""
        return lst.count(element)

    @staticmethod
    def unique(lst):
        """Get unique elements from list"""
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result

    @staticmethod
    def flatten(lst):
        """Flatten a nested list"""
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(BuiltinFunctions.flatten(item))
            else:
                result.append(item)
        return result
    
    @staticmethod
    def to_string(obj):
        """Convert object to string"""
        return str(obj)
    
    @staticmethod
    def to_number(obj):
        """Convert object to number"""
        try:
            if isinstance(obj, float):
                return obj
            return int(obj)
        except:
            return float(obj)
    
    @staticmethod
    def to_list(obj):
        """Convert object to list"""
        return list(obj)
    
    @staticmethod
    def to_dict(obj):
        """Convert object to dictionary"""
        if isinstance(obj, dict):
            return obj
        return {}
    
    # ═══════════════════════════════════════════════════════════════
    # GSE and Mother Equation Functions
    # دوال المعادلة الأم ونظام GSE
    # ═══════════════════════════════════════════════════════════════
    
    @staticmethod
    def GSEModel(beta=0.0, gamma=0.0):
        """
        Create a new GSE (Generalized Shape Equation) model.
        إنشاء نموذج معادلة شكل عام جديد.
        
        Args:
            beta: slope of linear component (ميل المكون الخطي)
            gamma: intercept of linear component (إزاحة المكون الخطي)
        
        Returns:
            GSEModel instance
        
        Example:
            model = GSEModel(0.5, 1.0)
            model.add_sigmoid(2.0, 3, 10.0, 0.0)
            y = model.evaluate([0.5, 1.0, 1.5])
        """
        from .gse import GSEModel as GSE
        return GSE(beta, gamma)
    
    @staticmethod
    def MotherEquation(object_id, object_name):
        """
        Create a Mother Equation object.
        إنشاء كائن معادلة أم.
        
        Args:
            object_id: unique identifier (معرف فريد)
            object_name: object name (اسم الكائن)
        
        Returns:
            MotherEquation instance
        
        Example:
            obj = MotherEquation("H001", "محمد")
            obj.add_property("الطول", 175, PropertyDomain.PHYSICAL, "cm")
            obj.add_state("الجوع", 0.5)
        """
        from .mother_equation import MotherEquation as ME
        return ME(object_id, object_name)
    
    @staticmethod
    def PropertyDomain(domain_name):
        """
        Get PropertyDomain enum value.
        الحصول على قيمة PropertyDomain.
        
        Args:
            domain_name: domain name (e.g., "PHYSICAL", "فيزيائي")
        
        Returns:
            PropertyDomain enum value
        """
        from .mother_equation import PropertyDomain as PD
        # Support both English and Arabic names
        mapping = {
            'PHYSICAL': PD.PHYSICAL,
            'فيزيائي': PD.PHYSICAL,
            'CHEMICAL': PD.CHEMICAL,
            'كيميائي': PD.CHEMICAL,
            'PSYCHOLOGICAL': PD.PSYCHOLOGICAL,
            'نفسي': PD.PSYCHOLOGICAL,
            'SOCIAL': PD.SOCIAL,
            'اجتماعي': PD.SOCIAL,
            'BIOLOGICAL': PD.BIOLOGICAL,
            'بيولوجي': PD.BIOLOGICAL,
        }
        return mapping.get(domain_name, PD.PHYSICAL)
    
    @staticmethod
    def create_example_human():
        """Create an example human object (إنشاء مثال إنسان)"""
        from .mother_equation import create_example_human as ceh
        return ceh()
    
    @staticmethod
    def create_example_tree():
        """Create an example tree object (إنشاء مثال شجرة)"""
        from .mother_equation import create_example_tree as cet
        return cet()
    
    @staticmethod
    def create_example_building():
        """Create an example building object (إنشاء مثال مبنى)"""
        from .mother_equation import create_example_building as ceb
        return ceb()
    
    @staticmethod
    def render_shape(mother_eq, x_range=(-10, 10), resolution=100):
        """
        Render the shape equation of a MotherEquation object.
        رسم معادلة الشكل لكائن معادلة أم.
        
        Args:
            mother_eq: MotherEquation instance
            x_range: tuple of (min, max) for x values
            resolution: number of points
        
        Returns:
            numpy array of y values
        
        Example:
            tree = create_example_tree()
            y_vals = render_shape(tree, (0, 10), 50)
        """
        return mother_eq.render_shape(x_range, resolution)
    
    # ═══════════════════════════════════════════════════════════════
    # Linguistic Equation Functions
    # دوال المعادلات اللغوية
    # ═══════════════════════════════════════════════════════════════
    
    @staticmethod
    def LinguisticEquation(entities, event, event_type="PHYSICAL_ACTION"):
        """
        Create a linguistic equation.
        إنشاء معادلة لغوية.
        
        Args:
            entities: dict of {entity_name: role}
            event: event/verb name
            event_type: type of event (default: PHYSICAL_ACTION)
        
        Returns:
            LinguisticEquation instance
        
        Example:
            eq = LinguisticEquation(
                {"محمد": Role.SUBJECT, "تفاحة": Role.OBJECT},
                "أكل",
                "PHYSICAL_ACTION"
            )
        """
        from .linguistic_equation import (
            LinguisticEquation as LE,
            Role, EventType
        )
        
        # Convert role strings to Role enum
        converted_entities = {}
        for name, role in entities.items():
            if isinstance(role, str):
                role_mapping = {
                    'SUBJECT': Role.SUBJECT,
                    'فاعل': Role.SUBJECT,
                    'OBJECT': Role.OBJECT,
                    'مفعول_به': Role.OBJECT,
                    'LOCATION': Role.LOCATION,
                    'مكان': Role.LOCATION,
                    'TIME': Role.TIME,
                    'زمان': Role.TIME,
                }
                role = role_mapping.get(role, Role.SUBJECT)
            converted_entities[name] = role
        
        # Convert event type
        if isinstance(event_type, str):
            type_mapping = {
                'PHYSICAL_ACTION': EventType.PHYSICAL_ACTION,
                'فعل_مادي': EventType.PHYSICAL_ACTION,
                'MENTAL_ACTION': EventType.MENTAL_ACTION,
                'فعل_عقلي': EventType.MENTAL_ACTION,
                'COMMUNICATION': EventType.COMMUNICATION,
                'تواصل': EventType.COMMUNICATION,
            }
            event_type = type_mapping.get(event_type, EventType.PHYSICAL_ACTION)
        
        return LE(
            entities=converted_entities,
            event=event,
            event_type=event_type
        )
    
    @staticmethod
    def Role(role_name):
        """
        Get Role enum value.
        الحصول على قيمة Role.
        """
        from .linguistic_equation import Role as R
        mapping = {
            'SUBJECT': R.SUBJECT,
            'فاعل': R.SUBJECT,
            'OBJECT': R.OBJECT,
            'مفعول_به': R.OBJECT,
            'LOCATION': R.LOCATION,
            'مكان': R.LOCATION,
        }
        return mapping.get(role_name, R.SUBJECT)
    
    @staticmethod
    def KnowledgeBase():
        """Create a new KnowledgeBase (إنشاء قاعدة معرفة جديدة)"""
        from .linguistic_equation import KnowledgeBase as KB
        return KB()
    
    @staticmethod
    def parse_sentence(sentence, kb=None):
        """
        Parse a natural language sentence into a linguistic equation.
        تحليل جملة طبيعية إلى معادلة لغوية.
        
        Args:
            sentence: Arabic sentence
            kb: KnowledgeBase instance (optional)
        
        Returns:
            LinguisticEquation or None
        
        Example:
            kb = KnowledgeBase()
            eq = parse_sentence("محمد أكل تفاحة", kb)
            print(eq.to_formal_notation())
        """
        from .linguistic_equation import LinguisticEquationParser, KnowledgeBase as KB
        
        if kb is None:
            kb = KB()
        
        parser = LinguisticEquationParser(kb)
        return parser.parse(sentence)
    
    @staticmethod
    def create_simple_equation(subject, event, obj=None, kb=None):
        """
        Create a simple linguistic equation quickly.
        إنشاء معادلة لغوية بسيطة بسرعة.
        
        Args:
            subject: subject/actor (الفاعل)
            event: verb/event (الفعل)
            obj: object (المفعول به) - optional
            kb: KnowledgeBase - optional
        
        Returns:
            LinguisticEquation
        
        Example:
            eq = create_simple_equation("محمد", "أكل", "تفاحة")
        """
        from .linguistic_equation import create_simple_equation as cse
        return cse(subject, event, obj, kb)
    
    # ═══════════════════════════════════════════════════════════════
    # GSE Learning Functions (if scipy available)
    # دوال التعلم لـ GSE
    # ═══════════════════════════════════════════════════════════════
    
    @staticmethod
    def learn(model_name, x_data, y_data, max_components=10, epsilon=1e-4, verbose=False):
        """
        Learn/fit a GSE model to data.
        تعلم نموذج GSE من البيانات.
        
        Args:
            model_name: name to store the model (اسم النموذج)
            x_data: input data (البيانات المدخلة)
            y_data: target data (البيانات المستهدفة)
            max_components: max sigmoid components (أقصى عدد مكونات)
            epsilon: convergence threshold (عتبة التقارب)
            verbose: print progress (طباعة التقدم)
        
        Returns:
            Fitted GSEModel
        
        Example:
            x = [0, 1, 2, 3, 4]
            y = [0, 1, 2, 3, 4]
            model = learn("linear_model", x, y, max_components=3, verbose=True)
        
        Note:
            Requires scipy to be installed.
        """
        if not GSE_FITTING_AVAILABLE:
            raise ImportError(
                "scipy is required for GSE fitting. "
                "Install it with: pip install scipy"
            )
        
        from .gse_fitting import GSEFitter
        from .gse import GSEModel as GSE
        
        fitter = GSEFitter(GSE())
        model = fitter.fit(x_data, y_data, max_components, epsilon, verbose)
        
        # Store in a global registry (could be enhanced)
        if not hasattr(BuiltinFunctions, '_model_registry'):
            BuiltinFunctions._model_registry = {}
        BuiltinFunctions._model_registry[model_name] = model
        
        return model
    
    @staticmethod
    def infer(model_name, x_value):
        """
        Infer/predict using a learned GSE model.
        الاستنباط/التنبؤ باستخدام نموذج GSE متعلم.
        
        Args:
            model_name: name of stored model (اسم النموذج)
            x_value: input value or array (قيمة أو مصفوفة مدخلة)
        
        Returns:
            Predicted y value(s)
        
        Example:
            # After learning a model
            y_pred = infer("linear_model", 2.5)
        """
        if not hasattr(BuiltinFunctions, '_model_registry'):
            raise ValueError(f"No model named '{model_name}' found. Use learn() first.")
        
        if model_name not in BuiltinFunctions._model_registry:
            raise ValueError(f"Model '{model_name}' not found in registry.")
        
        model = BuiltinFunctions._model_registry[model_name]
        
        # Convert to list if single value
        if not isinstance(x_value, (list, tuple)):
            import numpy as np
            x_value = [x_value]
            result = model.evaluate(x_value)
            return result[0] if len(result) == 1 else result
        
        return model.evaluate(x_value)

class LogicalBuiltins:
    """Built-in logical predicates"""
    
    @staticmethod
    def create_member_rules(engine):
        """Add member/2 predicate to logical engine"""
        # member(X, [X|_]).
        # member(X, [_|T]) :- member(X, T).
        pass
    
    @staticmethod
    def create_append_rules(engine):
        """Add append/3 predicate to logical engine"""
        # append([], L, L).
        # append([H|T1], L2, [H|T3]) :- append(T1, L2, T3).
        pass
    
    @staticmethod
    def create_length_rules(engine):
        """Add length/2 predicate to logical engine"""
        # length([], 0).
        # length([_|T], N) :- length(T, N1), N is N1 + 1.
        pass

