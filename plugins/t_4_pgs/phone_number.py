# developing
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.neededshits.cust_p_filters import f_onw_fliter
from phonenumbers import carrier, geocoder, timezone

def fetch_ph (ph):
  ph = phonenumbers.parse(ph)
  return carrier.name_for_number(ph, "en")
  return geocoder.description_for_number(ph, "en")
  return timezone.time_zones_for_number(ph)
