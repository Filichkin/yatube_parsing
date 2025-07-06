BOT_NAME = "yatube_parsing"

SPIDER_MODULES = ["yatube_parsing.spiders"]
NEWSPIDER_MODULE = "yatube_parsing.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ITEM_PIPELINES = {
    'yatube_parsing.pipelines.MondayPipeline': 300,
}
