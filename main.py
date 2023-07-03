##command line logged into linux operating system
##install the follwoing packages
##module load languages/python/3.9.15
##pip install --upgrade synapseclient
##pip install synapseutils
##go to working directory and open python interactively
import synapseclient
import synapseutils
import os
syn = synapseclient.Synapse()
token = #add token key to log into account
syn.login(authToken=token)
destination_folder = "/ukbb_protein_files/" #select destination foler
files = synapseutils.syncFromSynapse(syn, 'syn51365303', path=destination_folder) #add synapse ID for which project/data you would like, this example is for European discovery pQTLs
#see https://www.synapse.org/#!Synapse:syn51364943/wiki/622119 for more details and paper: https://doi.org/10.1101/2022.06.17.496443
