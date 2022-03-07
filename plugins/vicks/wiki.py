import logging
import re

import wikipedia
from telegram.ext import Updater, CommandHandler, Filters, CallbackQueryHandler

import keyboards.disambiguation_keyboard as dkb
from con import config

# Messages
FIND_OUT_MORE = '\n\n Find out more at '
HELP_MESSAGE = 'To wiki: \n\n /wiki [search input] \n\n'

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def callback_handler(update, context):
  query = update.callback_query
  callback_data = query.data

  try:
    if 'ERROR;DISAMBIGUATION;' in callback_data:
      search_input = re.match("ERROR;DISAMBIGUATION;(.+)", callback_data).group(1)
      page_result = wikipedia.page(search_input)
      summary = page_result.summary
      message = FIND_OUT_MORE + page_result.url
      query.edit_message_text(text=summary+message)
  except:
    query.edit_message_text(text="Whut? An unprecedented error has occurred.")


def wiki(update, context):
  user_input = re.match("\/wiki([@_\w]+|) (.+)", update.message.text).group(2)
  try:
    page_result = wikipedia.page(user_input)
    summary = page_result.summary
    message = FIND_OUT_MORE + page_result.url
    update.message.reply_text(summary+message)
  except wikipedia.exceptions.DisambiguationError as disambiguation:
    try:
      update.message.reply_text('Please choose:',
        reply_markup=dkb.create_disambiguation_keyboard(disambiguation.options))
    except:
      update.message.reply_text("There is disambiguity but an unprecedented error has occurred.")

  except wikipedia.exceptions.PageError as page_error:
    update.message.reply_text("Unable to find wiki page for \'" + user_input + "\'.")

  except wikipedia.exceptions.HTTPTimeoutError as http_timeout:
    update.message.reply_text("Time out! Mediawiki is giving me trouble...")

  except wikipedia.exceptions.RedirectError as redirect_error:
    update.message.reply_text("Baam! Redirection Error.")

  except wikipedia.exceptions.WikipediaException as wiki_exception:
    update.message.reply_text("Welp... Wiki base class error.")

  except:
    update.message.reply_text("Whut? An unprecedented error has occurred.")

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

