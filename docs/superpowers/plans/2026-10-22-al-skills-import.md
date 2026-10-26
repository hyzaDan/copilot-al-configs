# Import a audit AL skillů

Požadavek: začlenit AL-Copilot-Skills-Collection s minimem změn a posoudit každý cizí i dosavadní skill. Pracovat v aktuálním checkoutu; bez publikování a změn globální konfigurace.

- [x] Získat přesný upstream commit, licenci, úplný seznam skillů a současný stav projektu.
- [x] Prověřit obsah, duplicity, přenositelnost a podstatné chyby; nejisté platformní závěry ověřit v primárních zdrojích.
- [x] Přenést všech 39 balíčků včetně referencí, autorství a šablon. Zachovat původní těla; přidat odkaz na integrační omezení a upravit jen neplatná metadata/odkazy. Neprovádět cizí skripty. Zachovat stávajících 11 skillů.
- [x] Zaznamenat původ, commit, licence, vynechané cache soubory a hashe před/po úpravách; aktualizovat dokumentaci a verzi všech manifestů.
- [x] Vypracovat český report s 50 samostatnými verdikty, konkrétními důkazy a rozdílem mezi převzetím a doporučením pro běžné používání.
- [x] Ověřit metadata, soubory, odkazy, manifesty a integritu importu. Nezávisle prověřit, zda integrační pokyny správně zastaví nefunkční workflow. AL kompilaci a runtime neslibovat bez BC projektu.

Kontrola rizik: chybějící DOCX shared resources; nebezpečné či neúplné deploy/Dataverse skripty; kolize s původními skilly; příliš dlouhé descriptions; nedoložené API vzory. Import je revizní základ pro následné rozhodnutí, nikoli potvrzení správnosti všech upstream příkladů. Doporučení vyřadit není automatické mazání.

Výsledek: všech 50 vstupů validních; 228 souborů ověřeno proti upstream Git blobům, 189 bajtově shodných; 112 lokálních odkazů ve skillech, 6 manifestů 0.2.0. Report má 50 unikátních verdiktů. Nezávislá kontrola importu a tří statických směrovacích scénářů bez zbývajících závažných nálezů. Původních 11 skillů má nulový diff. Bez commit/push/reinstalace, AL kompilace nebo BC runtime testu.
