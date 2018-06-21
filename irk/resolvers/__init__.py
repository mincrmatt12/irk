from irk.resolvers.aptresolver import AptResolver
from irk.resolvers.customresolver import RegexResolver
from .pipresolver import PipResolver

ALL_RESOLVER_TYPES = [PipResolver, AptResolver, RegexResolver]