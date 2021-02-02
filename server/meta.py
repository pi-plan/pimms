from server.base import BaseHandler


class Meta(BaseHandler):
    async def get(self, version: str, zone_id: str = None):
        if version not in self.application.db.keys():
            self.error(404, "not found version meta.")
            return
        result = {
                "version": int(version),
                }
        if zone_id:
            for zone in self.application.db[version]["zones"]:
                if str(zone["zone_id"]) == zone_id:
                    result["data"] = zone
                    break
        else:
            result["data"] = self.application.db[version]
        self.succ(result)
