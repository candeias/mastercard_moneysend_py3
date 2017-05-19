#
# Copyright (c) 2016 MasterCard International Incorporated
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this list of
# conditions and the following disclaimer.
# Redistributions in binary form must reproduce the above copyright notice, this list of
# conditions and the following disclaimer in the documentation and/or other materials
# provided with the distribution.
# Neither the name of the MasterCard International Incorporated nor the names of its
# contributors may be used to endorse or promote products derived from this software
# without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
# SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
# TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS;
# OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
#


from mastercardapicore import Environment
from mastercardapicore import Config

class ResourceConfig(object):
	"""
	Configurable Resouces so that we can point to different environments
	"""
	name = "moneysend"
	override = None
	host = None
	context = None
	version = "1.0.4"
	environmentMap = Environment.mapping
	__initialized = False
	__instance = None

	def __init__(self):
		raise Exception("This is a singleton, you need to call ResourceConfig.getInstance() instead")

	def __new__(cls):
		bare_instance = object.__new__(cls)
		# you may want to have some common initialisation code here
		return bare_instance

	@staticmethod
	def getInstance():
		if ResourceConfig.__initialized == False:
			print("initilizing.... true")
			ResourceConfig.__initialized = True

			print("creating a new instance")
			tmpInstance = ResourceConfig.__new__(ResourceConfig)

			print("regestring a new instance")
			Config.registerResourceConfig(tmpInstance)
			tmpInstance.setEnvironment(Config.getEnvironment())

			print("saving instance")
			ResourceConfig.__instance = tmpInstance

		return ResourceConfig.__instance

	def getContext(cls):
		return cls.context

	def getHost(cls):
		if cls.override:
			return cls.override
		else:
			return cls.host

	def getVersion(cls):
		return cls.version

	def getName(cls):
		return cls.name

	def setEnvironment(cls,environment):
		if environment in list(cls.environmentMap.keys()):
			tuple = cls.environmentMap[environment]
			cls.host = tuple[0]
			cls.context = tuple[1]

	def setCustomEnvironment(cls,host,context):
		cls.host = host
		cls.context = context
