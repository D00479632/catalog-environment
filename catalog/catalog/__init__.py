from gymnasium.envs.registration import register 

from catalog.envs.catalog_env import CatalogEnv
from catalog.envs.catalog_model import Student
from catalog.envs.catalog_model import CatalogModel
from catalog.envs.catalog_model import getFullCatalog

register(
        # folderName/GYMname-version
        id="catalog/Catalog-v0",

        # path(catalog/envs):className
        entry_point="catalog.envs:CatalogEnv",

        # Automatic wrapper to truncate after 50 steps.
        max_episode_steps=50,
)
