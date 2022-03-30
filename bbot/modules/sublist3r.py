from .base import BaseModule


class dnsdumpster(BaseModule):

    watched_events = ["DOMAIN", "SUBDOMAIN"]
    produced_events = ["SUBDOMAIN"]

    def handle_event(self, event):
        # only process targets
        if not "target" in event.tags:
            return

        query = str(event.data).lower()

        results = self.helpers.request(
            f"https://api.sublist3r.com/search.php?domain={query}"
        )

        try:
            json = results.json()
            for hostname in json:
                if hostname in self.scan.target and not hostname == event:
                    self.emit_event(hostname, "SUBDOMAIN", event)
                else:
                    self.debug(f"Invalid subdomain: {hostname}")
        except Exception as e:
            self.error(f"Error retrieving sublist3r domains: {e}")