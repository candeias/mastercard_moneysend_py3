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


from mastercardapicore import BaseObject
from mastercardapicore import RequestMap
from mastercardapicore import OperationConfig
from mastercardapicore import OperationMetadata
from .resourceconfig import ResourceConfig

class CardMapping(BaseObject):
	"""
	
	"""

	__config = {
		
		"93f59d06-df06-48ab-9633-208d0da481ca" : OperationConfig("/moneysend/v3/mapping/card", "create", [], []),
		
		"25791dea-df4a-4e1f-8418-48d7cf03ee8b" : OperationConfig("/moneysend/v3/mapping/card/{mappingId}", "delete", [], []),
		
		"ae8f3d37-0dd6-44ec-ac9b-16dad6a65ea0" : OperationConfig("/moneysend/v3/mapping/subscriber", "update", [], []),
		
		"2bad23fe-1ff5-4ff9-bf32-74b620ccfb1e" : OperationConfig("/moneysend/v3/mapping/card", "update", [], []),
		
		"d9e2cf3c-6d50-4a0f-9f9c-d48d1290cb57" : OperationConfig("/moneysend/v3/mapping/card/{mappingId}", "update", [], []),
		
	}

	def getOperationConfig(self,operationUUID):
		if operationUUID not in self.__config:
			raise Exception("Invalid operationUUID: "+operationUUI)

		return self.__config[operationUUID]

	def getOperationMetadata(self):
		return OperationMetadata(ResourceConfig.getInstance().getVersion(), ResourceConfig.getInstance().getHost(), ResourceConfig.getInstance().getContext())


	@classmethod
	def create(cls,mapObj):
		"""
		Creates object of type CardMapping

		@param Dict mapObj, containing the required parameters to create a new object
		@return CardMapping of the response of created instance.
		@raise ApiException: raised an exception from the response status
		"""
		return BaseObject.execute("93f59d06-df06-48ab-9633-208d0da481ca", CardMapping(mapObj))









	@classmethod
	def deleteById(cls,id,map=None):
		"""
		Delete object of type CardMapping by id

		@param str id
		@return CardMapping of the response of the deleted instance.
		@raise ApiException: raised an exception from the response status
		"""

		mapObj =  RequestMap()
		if id:
			mapObj.set("id", id)

		if map:
			if (isinstance(map,RequestMap)):
				mapObj.setAll(map.getObject())
			else:
				mapObj.setAll(map)

		return BaseObject.execute("25791dea-df4a-4e1f-8418-48d7cf03ee8b", CardMapping(mapObj))

	def delete(self):
		"""
		Delete object of type CardMapping

		@return CardMapping of the response of the deleted instance.
		@raise ApiException: raised an exception from the response status
		"""
		return BaseObject.execute("25791dea-df4a-4e1f-8418-48d7cf03ee8b", self)




	def deleteSubscriberID(self):
		"""
		Updates an object of type CardMapping

		@return CardMapping object representing the response.
		@raise ApiException: raised an exception from the response status
		"""
		return BaseObject.execute("ae8f3d37-0dd6-44ec-ac9b-16dad6a65ea0", self)






	def read(self):
		"""
		Updates an object of type CardMapping

		@return CardMapping object representing the response.
		@raise ApiException: raised an exception from the response status
		"""
		return BaseObject.execute("2bad23fe-1ff5-4ff9-bf32-74b620ccfb1e", self)






	def update(self):
		"""
		Updates an object of type CardMapping

		@return CardMapping object representing the response.
		@raise ApiException: raised an exception from the response status
		"""
		return BaseObject.execute("d9e2cf3c-6d50-4a0f-9f9c-d48d1290cb57", self)






