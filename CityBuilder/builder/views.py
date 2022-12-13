from django.shortcuts import render
from django.http import HttpResponse
from .models import Race, CityPrefix, CitySuffix, BusinessPrefix, BusinessSuffix, BusinessInventory, NPCtraits, VillagerLastNames, VillagerFirstNames
from django.views.generic import TemplateView
import random
from itertools import chain
# Create your views here.
class HomeView(TemplateView):
    template_name = "builder/home.html"

class DwarfSizeSelect(TemplateView):
    template_name = "builder/dwarfsize.html"

class DwarfCity(TemplateView):
    template_name = "builder/dwarfcity.html"

    def get_context_data(self, **kwargs):
        #City name generator
        context = super().get_context_data(**kwargs)
        dwarf_pre_list = CityPrefix.objects.filter(race__race__contains="Dwarf")
        random_dwarf_pre = random.choice(dwarf_pre_list)
        context["dwarfpre"] = random_dwarf_pre
        dwarf_suf_list = CitySuffix.objects.filter(race__race__contains="Dwarf")
        random_dwarf_suf = random.choice(dwarf_suf_list)
        context["dwarfsuf"] = random_dwarf_suf
        #population size and guard size
        context["guard_size"] = random.randint(300,500)
        context["population"] = random.randint(1000,2500)
        #NPC Traits and names
        context["common_traits"] = list(NPCtraits.objects.filter(type="Common"))
        context["guard_traits"] = list(NPCtraits.objects.filter(type="Guard"))
        context["business_traits"] = list(NPCtraits.objects.filter(type="Business"))
        context["official_traits"] = list(NPCtraits.objects.filter(type="Official"))
        #local NPCs and Town Guard
        local_first = list(VillagerFirstNames.objects.filter(race__race__contains="Dwarf"))
        context["local_first"] = random.sample(local_first, 3)
        context["guard_first"] = random.sample(local_first, 3)
        local_last = list(VillagerLastNames.objects.filter(race__race__contains="Dwarf"))
        context["local_last"] = random.sample(local_last, 3)
        context["guard_last"] = random.sample(local_last, 3)
        #foreign NPCS
        races = Race.objects.exclude(race__contains="Dwarf")
        race1 = random.choice(races)
        race2 = random.choice(races)
        race3 = random.choice(races)
        foreign_first1 = list(VillagerFirstNames.objects.filter(race__race=race1.race))
        foreign_last1 = list(VillagerLastNames.objects.filter(race__race=race1.race))
        rand_first1 = random.sample(foreign_first1, 2)
        rand_last1 = random.sample(foreign_last1, 2)
        context["foreign_names1"] = zip(rand_first1, rand_last1)
        foreign_first2 = list(VillagerFirstNames.objects.filter(race__race=race2.race))
        foreign_last2 = list(VillagerLastNames.objects.filter(race__race=race2.race))
        rand_first2 = random.sample(foreign_first2, 2)
        rand_last2 = random.sample(foreign_last2, 2)
        context["foreign_names2"] = zip(rand_first2, rand_last2)
        foreign_first3 = list(VillagerFirstNames.objects.filter(race__race=race3.race))
        foreign_last3 = list(VillagerLastNames.objects.filter(race__race=race3.race))
        rand_first3 = random.sample(foreign_first3, 2)
        rand_last3 = random.sample(foreign_last3, 2)
        context["foreign_names3"] = zip(rand_first3, rand_last3)
        #Permanent Businesses (tavern, inn, blacksmith, healer)
        #Tavern
        tavern_pres = BusinessPrefix.objects.filter(type__type__contains="Tavern")
        context["tavernpre"] = random.choice(tavern_pres)
        tavern_suf = BusinessSuffix.objects.filter(type__type__contains="Tavern")
        context["tavernsuf"] = random.choice(tavern_suf)
        inventory = list(BusinessInventory.objects.filter(business_type__type="Tavern"))
        context["inventory1"] = random.sample(inventory, 2)
        shop_keeper_first = VillagerFirstNames.objects.filter(race__race__contains="Dwarf")
        context["tav_first"] = random.choice(shop_keeper_first)
        shop_keeper_last = VillagerLastNames.objects.filter(race__race__contains="Dwarf")
        context["tav_last"] = random.choice(shop_keeper_last)
        #Inn
        inn_pres = BusinessPrefix.objects.filter(type__type__contains="Inn")
        context["innpre"] = random.choice(inn_pres)
        inn_suf = BusinessSuffix.objects.filter(type__type__contains="Inn")
        context["innsuf"] = random.choice(inn_suf)
        inventory = list(BusinessInventory.objects.filter(business_type__type="Inn"))
        context["inventory2"] = random.sample(inventory, 2)
        context["inn_first"] = random.choice(shop_keeper_first)
        context["inn_last"] = random.choice(shop_keeper_last)
        #Blacksmith
        bs_pres = BusinessPrefix.objects.filter(type__type__contains="Blacksmith")
        context["bs_pre"] = random.choice(bs_pres)
        bs_suf = BusinessSuffix.objects.filter(type__type__contains="Blacksmith")
        context["bs_suf"] = random.choice(bs_suf)
        inventory = list(BusinessInventory.objects.filter(business_type__type="Blacksmith"))
        context["inventory3"] = random.sample(inventory, 2)
        context["bs_first"] = random.choice(shop_keeper_first)
        context["bs_last"] = random.choice(shop_keeper_last)
        #first random Business generator excluding permanents
        business_pres = BusinessPrefix.objects.exclude(type__type="Tavern").exclude(type__type="Inn").exclude(type__type="Blacksmith")
        rand_business_pre = random.choice(business_pres)
        context["randpre1"] = rand_business_pre
        business_suf = BusinessSuffix.objects.filter(type__type=rand_business_pre.type)
        context["randsuf1"] = random.choice(business_suf)
        inventory2 = list(BusinessInventory.objects.filter(business_type__type=rand_business_pre.type))
        context["randinventory1"] = random.sample(inventory2, 2)
        context["rand1_first"] = random.choice(shop_keeper_first)
        context["rand1_last"] = random.choice(shop_keeper_last)
        return context
