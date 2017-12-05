#!/usr/bin/env python.
'''
    File name: generate_dyes_for_valk_helms.py
    Date created: December 4, 2017
    Python version: 3.6.1
    Purpose:
        Generates code to be used by a dye npc so that people can
        change the color of their valkyrie helms.
    Author: Phuc H Duong
    Website: phuchduong.io
    Linkedin: https://www.linkedin.com/in/phuchduong/
'''
from os.path import isdir

valk_helm_ids = [
    49000, 49001, 49002, 49003, 49004, 49005, 49006, 49007, 49008, 49009, 49010, 49011, 49012, 49013,
    49014, 49015, 49016, 49017, 49018, 49019, 49020, 49021, 49022, 49023, 49024, 49025, 49026, 49027,
    49028, 49029, 49030, 49031, 49032, 49033, 49034, 49035, 49036, 49037, 49038, 49039, 49040, 49041,
    49042, 49043, 49044, 49045, 49046, 49047, 49048, 49049, 49050, 49051, 49052, 49053, 49054, 49055,
    49056, 49057, 49058, 49059, 49060, 49061, 49062, 49063, 49064, 49065, 49066, 49067, 49068, 49069,
    49070, 49071, 49072, 49073, 49074, 49075, 49076, 49077, 49078, 49079, 49080, 49081, 49082, 49083,
    49084, 49085, 49086, 49087, 49088, 49089, 49090, 49091, 49092, 49093, 49094, 49095, 49096, 49097,
    49098, 49099, 49100, 49101, 49102, 49103, 49104, 49105, 49106, 49107, 49108, 49109, 49110, 49111,
    49112, 49113, 49114, 49115, 49116, 49117, 49118, 49119, 49120, 49121, 49122, 49123, 49124, 49125,
    49126, 49127, 49128, 49129, 49130, 49131, 49132, 49133, 49134, 49135, 49136, 49137, 49138, 49139,
    49140, 49141, 49142, 49143, 49144, 49145, 49146, 49147, 49148, 49149, 49150, 49151, 49152, 49153,
    49154, 49155, 49156, 49157, 49158, 49159, 49160, 49161, 49162, 49163, 49164, 49165, 49166, 49167,
    49168, 49169, 49170, 49171, 49172, 49173, 49174, 49175]

if isdir("C:/repos"):
    base_dir = "C:/repos/"
elif isdir("D:/repos/"):
    base_dir = "D:/repos/"  # change this to your own

out_folder_path = "essencero_restoration/build_items/outputs/"
filename = "valkyrie_ids.txt"

file_path = base_dir + out_folder_path + filename

f = open(file=file_path, mode="w")

current_combinations = []

for first_id in valk_helm_ids:
    first_id = str(first_id)
    for second_id in valk_helm_ids:
        second_id = str(second_id)
        combo_id = first_id + second_id
        if combo_id not in current_combinations and second_id != first_id:
            f.write("\tDyes(" + first_id + "," + second_id + ",0,0,0,0);\n")
            current_combinations.append(combo_id)
