# Finální konsolidace AL skillů — 23. 10. 2026

Verze **0.3.0** obsahuje **29 skillů**: 11 původních AL workflow, 16 úzkých BC specializací, `al-documentation` a diagnostiku instrukcí BC AI agenta. Z původních 50 vstupů má 26 zachovaný samostatný název, 19 je sloučeno a 5 vyřazeno. Nové společné názvy jsou `bc-api-design`, `bc-app-lifecycle` a `al-documentation`.

Doporučuji tuto sadu pro pilot v konkrétním AL projektu. Je menší a její používaný obsah obsahuje opravy přímo. Plošné firemní nasazení ještě vyžaduje ověřit skutečné načtení v používaných hostitelích, jejich nástroje a cílové BC runtime scénáře níže. Kontrola textu ani dvě kompilované ukázky nejsou certifikací všech budoucích implementací.

## Rozsah a principy

Základ zůstává v `al-*`: coding/review/debugging/testing/context mají jeden vlastník workflow. Bezpečnostní a výkonnostní review zůstala oddělená kvůli odlišným spouštěčům. API page/query a install/upgrade jsou společné rozhodovací workflow s referencemi. Batching je pod Job Queue, report selection pod reports, wizard pod setup a coupling UI pod Dataverse mapping.

Malá změna nevyžaduje dokumentační řetězec, nový rozhovor, schválení již autorizované práce ani povinné delegování. Původní konvence pojmenování, affixů, placeholderů, cílení buildu a en-US → cs-CZ jsou zachovány. `SingleInstance` se řídí požadovanou životností stavu a výslovnou politikou projektu; starý plošný default byl odstraněn.

Specializace obsahují postup a omezení, nikoli tvrzení, že každá šablona je hotová pro libovolnou verzi BC. ID, názvy, cesty, prefixy, event signatury a přístupové modely se zjišťují v cílovém projektu. Nefunkční skripty a staré šablony nejsou v aktivní sadě ani v jiném discovery adresáři.

## Mapa všech 50 vstupů

„Ponechán“ znamená zachovaný účel/název, nikoli neměnné původní bajty. „Vyřazen“ se týká workflow; krátká obecná znalost potřeby schématu či inventury API může zůstat v příbuzném skillu, bez původního generátoru/frameworku.

| Původní skill | Výsledek | Aktivní cíl | Důvod |
| --- | --- | --- | --- |
| `al-bc-solution-review` | Ponechán | [al-bc-solution-review](../skills/al-bc-solution-review/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-build-validation` | Ponechán | [al-build-validation](../skills/al-build-validation/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-coding-standards` | Ponechán | [al-coding-standards](../skills/al-coding-standards/SKILL.md) | Zachováno projektové pojmenování; SingleInstance dle lifetime/politiky, nikoli povinně. |
| `al-debugging-methodology` | Ponechán | [al-debugging-methodology](../skills/al-debugging-methodology/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-performance-review` | Ponechán | [al-performance-review](../skills/al-performance-review/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-project-context-bootstrap` | Ponechán | [al-project-context-bootstrap](../skills/al-project-context-bootstrap/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-security-review` | Ponechán | [al-security-review](../skills/al-security-review/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-solution-architecture` | Ponechán | [al-solution-architecture](../skills/al-solution-architecture/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-symbol-lookup` | Ponechán | [al-symbol-lookup](../skills/al-symbol-lookup/SKILL.md) | Zachován úzký původní AL workflow; pouze relevantní reference a konkrétní důkazy. |
| `al-testing` | Ponechán | [al-testing](../skills/al-testing/SKILL.md) | Zachováno oddělení authored/compiled/executed; přidány handlery a reálná izolace. |
| `al-translation-phase` | Ponechán | [al-translation-phase](../skills/al-translation-phase/SKILL.md) | Zachován en-US → cs-CZ a izolovaný worker; upřesněna dostupnost NAB/XML cesty. |
| `bc-agent-instructions-debugger` | Ponechán | [bc-agent-instructions-debugger](../skills/bc-agent-instructions-debugger/SKILL.md) | Úzká BC AI specializace; opravené guards a odstraněn vymyšlený parser kontrakt. |
| `bc-al-bug-fix` | Sloučen | [al-debugging-methodology](../skills/al-debugging-methodology/SKILL.md) | Jedna diagnostika; převzaty AL pasti, odstraněny chybné load/trigger rady. |
| `bc-al-code-reviewer` | Sloučen | [al-bc-solution-review](../skills/al-bc-solution-review/SKILL.md) | Jedno review; priorita důkazu před checklistem, odstraněny falešné povinnosti. |
| `bc-al-project-context` | Sloučen | [al-project-context-bootstrap](../skills/al-project-context-bootstrap/SKILL.md) | Volitelný kontext/handoff a ADR bez povinného zápisu každé relace. |
| `bc-api-page-generator` | Sloučen | [bc-api-design](../skills/bc-api-design/SKILL.md) | Jedna volba API page/query a společný kontrakt; opravené bound actions. |
| `bc-api-query-generator` | Sloučen | [bc-api-design](../skills/bc-api-design/SKILL.md) | Sdílí API kontrakt; specifika read-only query zůstala v referenci. |
| `bc-approval-workflow-generator` | Ponechán | [bc-approval-workflow-generator](../skills/bc-approval-workflow-generator/SKILL.md) | Specifické workflow registrace, reakce a rekonstruování knihovny. |
| `bc-attachments-generator` | Ponechán | [bc-attachments-generator](../skills/bc-attachments-generator/SKILL.md) | Specifický attachment lifecycle a úplné klíče při kopii/mazání. |
| `bc-batch-processing` | Sloučen | [bc-job-queue](../skills/bc-job-queue/SKILL.md) | Dávky, checkpoint a restart jsou jedním workflow s Job Queue. |
| `bc-business-events-generator` | Ponechán | [bc-business-events-generator](../skills/bc-business-events-generator/SKILL.md) | Rozlišení interních a externích událostí, transakce a bezpečný payload. |
| `bc-cds-page-generator` | Sloučen | [bc-dataverse-mapping-generator](../skills/bc-dataverse-mapping-generator/SKILL.md) | Coupling UI má vlastní referenci v Dataverse workflow. |
| `bc-dataverse-entity-generator` | Vyřazen | — | Vyřazeny nebezpečné skripty a neověřený generátor; potřeba cílového Dataverse schématu zůstává v mapping skillu. |
| `bc-dataverse-mapping-generator` | Ponechán | [bc-dataverse-mapping-generator](../skills/bc-dataverse-mapping-generator/SKILL.md) | Užitečné ownership/sync/coupling rozhodování bez cizích helperů. |
| `bc-field-propagation` | Ponechán | [bc-field-propagation](../skills/bc-field-propagation/SKILL.md) | Posting/archive/copy matice a zachování vlastních transformací. |
| `bc-install-codeunit-generator` | Sloučen | [bc-app-lifecycle](../skills/bc-app-lifecycle/SKILL.md) | Install a upgrade sdílejí data lifecycle, ale zachovávají odlišné triggery. |
| `bc-isolated-storage-generator` | Ponechán | [bc-isolated-storage-generator](../skills/bc-isolated-storage-generator/SKILL.md) | SecretText, explicitní scope a šifrované uložení bez plaintext fallbacku. |
| `bc-job-queue` | Ponechán | [bc-job-queue](../skills/bc-job-queue/SKILL.md) | Restart, identita background uživatele a retry/recurrence mají konkrétní BC specifika. |
| `bc-manifest-handoff-generator` | Vyřazen | — | Cizí ALDC/CIRCE/DELFOS pipeline není dodána; obecná inventura API je volitelně v dokumentaci. |
| `bc-matrix-page-generator` | Ponechán | [bc-matrix-page-generator](../skills/bc-matrix-page-generator/SKILL.md) | Omezený počet sloupců, perioda, filtry a drilldown jsou úzká specializace. |
| `bc-number-series-generator` | Ponechán | [bc-number-series-generator](../skills/bc-number-series-generator/SKILL.md) | Moderní No. Series, ruční číslo, AssistEdit a souběh číslování. |
| `bc-pricing-refactor` | Ponechán | [bc-pricing-refactor](../skills/bc-pricing-refactor/SKILL.md) | Specifická migrace na pricing engine a správný Handler/Method vztah. |
| `bc-report-selection-generator` | Sloučen | [bc-reports](../skills/bc-reports/SKILL.md) | Specifické zapojení výběru reportů v samostatné referenci. |
| `bc-reports` | Ponechán | [bc-reports](../skills/bc-reports/SKILL.md) | Dataset/layout a tisk aktuálního dokladu vyžadují samostatnou znalost. |
| `bc-setup-table-generator` | Ponechán | [bc-setup-table-generator](../skills/bc-setup-table-generator/SKILL.md) | Singleton lifecycle, bezpečná konfigurace a volitelný wizard. |
| `bc-setup-wizard-generator` | Sloučen | [bc-setup-table-generator](../skills/bc-setup-table-generator/SKILL.md) | Wizard je volitelná reference setup workflow, včetně souběžných změn. |
| `bc-table-dimensions-generator` | Ponechán | [bc-table-dimensions-generator](../skills/bc-table-dimensions-generator/SKILL.md) | Dimension Set ID a validace zkratek mají vlastní platformní pravidla. |
| `bc-telemetry-generator` | Ponechán | [bc-telemetry-generator](../skills/bc-telemetry-generator/SKILL.md) | Ověřený producent/KQL kontrakt a ochrana obchodních dat. |
| `bc-test-codeunit-generator` | Sloučen | [al-testing](../skills/al-testing/SKILL.md) | Generování testů, handlery a skutečná izolace patří do jednoho workflow. |
| `bc-upgrade-codeunit-generator` | Sloučen | [bc-app-lifecycle](../skills/bc-app-lifecycle/SKILL.md) | Upgrade tags, company scope a bezpečná migrace ve společném skillu. |
| `documentation-bc-analysis-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `documentation-bc-architecture-generator` | Sloučen | [al-solution-architecture](../skills/al-solution-architecture/SKILL.md) | Převzaty BC rozhodovací hranice a ADR; cizí formální pipeline odstraněna. |
| `documentation-bc-ccn-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `documentation-bc-md-to-docx-converter` | Vyřazen | — | Nefunkční konvertor, chybějící registry, nekompatibilní šablony a JSON kontrakt; nový renderer není cílem. |
| `documentation-bc-phase-plan-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `documentation-bc-release-note-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `documentation-bc-technical-spec-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `documentation-bc-user-story-generator` | Sloučen | [al-documentation](../skills/al-documentation/SKILL.md) | Volba požadovaného artefaktu v jedné referenci; bez duplicitních interview a nedodaného registry. |
| `onprem-remote-deploy` | Vyřazen | — | Bezpečný přenos a kontext služby nebyly implementovány; odstraněn nefunkční deployment návod. |
| `skill-contribution-assistant` | Vyřazen | — | Nástroj přispívání do cizí kolekce není každodenní AL schopnost. |

## Konkrétní nálezy a jejich vypořádání

Podrobný původní důkaz včetně cest/řádků je v [auditu 0.2.0](skill-audit-2026-10-22.md). Níže je stav v aktivní sadě; žádný řádek není odložené varování vedle původního chybného příkladu.

| Nález původního auditu | Vypořádání v 0.3.0 |
| --- | --- |
| API: UI action zaměněná za bound action, neexistující helpery, nesprávná custom URL | Původní ukázky odstraněny. [API design](../skills/bc-api-design/SKILL.md) rozlišuje publisher/group/version a `[ServiceEnabled]`/`WebServiceActionContext`. |
| API query: dvakrát DataItemTableFilter, neúplné joiny | [Query reference](../skills/bc-api-design/references/queries.md) používá jednu kombinovanou deklaraci a úplnou identitu dokumentu. |
| Approval: nedeklarovaná entity proměnná, nekonzistentní status pole, UI jako jediná ochrana | Chybné šablony odstraněny; [approval](../skills/bc-approval-workflow-generator/SKILL.md) vyžaduje jednotné schéma, deklarace a vynucení i mimo UI. Zachována rekonstrukce workflow knihovny. |
| Attachments: mazání/kopie jen Table ID + No. | Nebezpečné recepty odstraněny; [attachments](../skills/bc-attachments-generator/SKILL.md) vyžadují bezeztrátové mapování úplného vlastníka včetně typu a řádku. Links/notes mají vlastní identitu. |
| Batch/Job Queue: pokusy zaměněné za úspěšné dávky, BatchLimit bez ukončení, plošné Modify(false) | [Job Queue](../skills/bc-job-queue/SKILL.md) a batching reference oddělují retry, další úspěšnou dávku, terminální stav, checkpoint a nejistý externí výsledek. Triggery se volí podle invariantu. |
| Business events: vymyšlený publisher a Item.OnModify jako důkaz změny zásoby | Obě ukázky odstraněny. [Business events](../skills/bc-business-events-generator/SKILL.md) vyžadují reálný publisher/transition, FlowField zdroj a transakční/consumer kontrakt. |
| Dataverse: chybné určení root, hromadný přesun AL s Force, nedodané BCS helpery, ID scan jen v src/Page | Generační skripty odstraněny. [Mapping](../skills/bc-dataverse-mapping-generator/SKILL.md) pracuje s cílovým schématem/symboly; coupling reference řeší celý projekt, identitu i Cancel bez změny vazby. |
| Field propagation: povinně stejná ID, mazání subscriberů podle TransferFields | [Propagation](../skills/bc-field-propagation/SKILL.md) rozlišuje field-number copy a explicitní mapping, zachovává transformace/validaci a ověřuje okamžik persistence i více faktur. |
| Bug-fix/reviewer: FlowField v SetLoadFields, nenačtené pole údajně vrací nulu, chybná signatura údajně tiše ignorována | Vadné reference odstraněny. [Record access](../skills/al-debugging-methodology/references/record-access.md) popisuje normal-only loading, JIT, CalcFields a ověření subscriberu. |
| Reviewer: plošné inherent permissions/entitlements a nesprávná vazba na PTE0001 | Odstraněna falešná podmínka. [Coding](../skills/al-coding-standards/SKILL.md) a [review](../skills/al-bc-solution-review/SKILL.md) vyžadují konkrétní oprávnění/analyzátor a důkaz problému. |
| Vlastní SingleInstance default | Plošný default odstraněn; [lifetime reference](../skills/al-coding-standards/references/subscriber-lifetime.md) rozlišuje platformní false, statické/manuální instance a výslovnou lokální politiku. |
| Install: CompanyName v SystemMetadata, přepis zákaznického setupu | Vadná ukázka odstraněna; [lifecycle](../skills/bc-app-lifecycle/SKILL.md) rozlišuje fresh install, reinstall, upgrade a novou společnost, zachovává hodnoty zákazníka. |
| Upgrade: RestoreArchiveData jako recovery a plošné Modify(false) | Zastaralý recept odstraněn; [migration](../skills/bc-app-lifecycle/references/migration-decisions.md) řeší identitu, tag až po úspěchu, explicitní validaci a commit pouze v podporovaném kontextu. |
| Matrix: libovolné dynamické sloupce, plošný interview, tvrzení production-ready | Nahrazeno [omezenými sloty a konkrétními rozhodnutími](../skills/bc-matrix-page-generator/SKILL.md): osy, období, clearing, neaditivní součty, drilldown/export filtry. |
| No. Series: AssistEdit bez true | [Number series](../skills/bc-number-series-generator/SKILL.md) obsahuje deklarovaný helper s true při úspěchu, bez změny caller stavu při Cancel. Moderní API ověřeno v Microsoft dokumentaci, cílové symbols stále nutné. |
| Pricing: neověřené interface fragmenty a registrace na Method místo Handler | Šablony odstraněny, [pricing](../skills/bc-pricing-refactor/SKILL.md) opravuje Handler/Method vztah, zachovává skutečné cenové podmínky a migrační/regresní matici. |
| Reports: neomezený tisk aktuálního dokladu a neúplný header-line join | [Reports](../skills/bc-reports/SKILL.md) a selection reference vyžadují úplný PK; SetRecFilter má caveat aktuálního klíče. Žádný plošný RDLC layout či pevný GetData index. |
| Setup: Masked Text jako šifrování, page Read místo Execute | [Setup](../skills/bc-setup-table-generator/SKILL.md) odděluje UI a úložiště, tabledata a execute oprávnění. Plaintext API-key šablona odstraněna. |
| Isolated storage: tichý fallback Set při selhání SetEncrypted | Odstraněn. [Storage](../skills/bc-isolated-storage-generator/SKILL.md) používá SecretText dle runtime, explicitní scope, kapacitu a sanitizovanou chybu; žádná truncation tokenu. |
| Wizard: stale whole-record TransferFields přepisuje souběžné změny | [Assisted setup](../skills/bc-setup-table-generator/references/assisted-setup.md) při Finish znovu načte, porovná vlastněná pole a aktualizuje jen je. ExpectedDuration správně v minutách. |
| Dimensions: cizí cesty/ID a OnAfterValidate na novém page fieldu | [Dimensions](../skills/bc-table-dimensions-generator/SKILL.md) opravuje trigger, rozlišuje default dimensions a set, výslovně odděluje změnu setu od combination/value-posting checks. |
| Telemetry: formátovaný Duration versus numerické KQL, raw chyby/obchodní identifikátory jako SystemMetadata | [Producer/KQL](../skills/bc-telemetry-generator/references/producer-and-kql.md) má numerické ms přes BigInteger, správné AL/al prefixy a pouze technická data. |
| Testy: slib automatického rollbacku každého testu | [Isolation reference](../skills/al-testing/references/handlers-and-isolation.md) uvádí Disabled/Codeunit/Function a externí side effects mimo DB rollback. Fresh install ověřuje reálnou lifecycle cestou. |
| BC AI agent: obrácený guard, povinné RGI/7 guidelines a simulace vydávaná za runtime | Vadné příklady odstraněny; [instruction checks](../skills/bc-agent-instructions-debugger/references/instruction-checks.md) požadují obě větve guardu a timeline evidence, nikoli vymyšlenou gramatiku. |
| Kontext: handoff po každé delší relaci, další souhlas k běžným zápisům, nejnovější soubor bez verze | Sloučeno do [volitelného kontextu](../skills/al-project-context-bootstrap/SKILL.md) s app/revision/source evidencí. |
| Dokumentační rodina: registry/helpery chybí, JSON/template/heading kontrakty nesouhlasí, Czech renderer není dodán | Celá závislá pipeline včetně DOCX skriptů/šablon odstraněna. [Documentation](../skills/al-documentation/SKILL.md) generuje jen požadovaný artefakt ve formátu projektu; žádný falešný Word export. |
| Dokumentace: pevné počty otázek/ADR/fází, cizí sazby a author/approval údaje | Odstraněny. Zůstala návaznost business → technická kritéria → skutečné ověření a release range. |
| Manifest handoff: ALDC/CIRCE/DELFOS a nedodaný mapping skill | Workflow vyřazeno. Volitelný inventář API v dokumentaci odlišuje návrh, build, deploy a dosažitelný endpoint/MCP tool. |
| On-prem deploy: kopie vydávaná za publish/sync/upgrade, SSH quoting/identita/scheduled-task/secret rizika | Celý skill i skripty vyřazeny. Nic se nenasazovalo a nevznikl náhradní deployment systém. |
| Contribution assistant: cizí governance a releaseplan | Vyřazen; nevynucuje se při AL vývoji. |
| Hosté: staré modelové názvy/rozbité worker odkazy, návod zaměněný za registraci | [Model routing](model-routing.md), README a agent odkazy sjednoceny. Copilot agent není automaticky Codex worker. NAB i XML fallback běží v izolovaném workeru. |
| Balík: host-specific SKILL metadata, hash drift CRLF/LF, vadná detekce cest | Osm volitelných metadata hintů odstraněno ze sdílených SKILL; agent invocation controls zachovány. LF vynucuje .gitattributes a validátor. Opraven regex HTTPS a přidány pozitivní/negativní testy. |

## Zmenšení a zachování znalostí

| Metrika v `skills/` | Před | Po |
| --- | ---: | ---: |
| Skilly | 50 | 29 |
| Soubory | 243 | 56 |
| Řádky entrypointů | 12843 | 957 |
| Řádky všech Markdown podkladů | 35412 | 1578 |
| Bajty všech souborů | 43372877 | 142970 |

Počet řádků je fyzická velikost souborů, nikoli tokeny, náklady nebo latence. Největší pokles bajtů pochází z odstranění Word šablon. Nezávislé review uvádí zachované konkrétní znalosti u všech 29 skillů; viz [obsahový report](validation/2026-10-23-final-content-review.md).

## Ověření a porovnání chování

- **Struktura a integrita:** 29 skillů, 56 aktivních souborů, všech 50 dispozic, lokální odkazy a šest manifestů 0.3.0. Raw Git blobs všech 228 původně importovaných souborů a přesná MIT licence porovnány s pinned upstream commitem. Udržované soubory mají vlastní hashe; není tvrzena shoda s upstreamem.
- **Metadata:** oficiální `skill-creator/quick_validate.py`: **29/29 PASS** po odstranění nepřenosných hintů. Výsledek a fault-injection testy zachycuje [technický log](validation/2026-10-23-package-checks.txt).
- **Validátor: 17/17 PASS.** Testy mění jen dočasné kopie balíčku; zkoušejí změněný/chybějící soubor, cizí discovery cestu, neplatný odkaz, YAML duplicitu, chybějící dispozici, rozdílnou verzi/routing/MCP, licenci, HTTPS versus Windows cesty a CRLF. Nejde o AL runtime testy.
- **Nezávislé obsahové review:** druhý agent přečetl 29 SKILL a 27 referencí. Žádný potvrzený věcný AL blocker; dva přesnější limity migrace/dimenzí doplněny. Všechny 66 odlišné externí URL dostupné HTTP 200. To ověřuje dostupnost zdroje, nikoli automaticky pravdivost všech tvrzení. Nezávisle nalezená chyba regexu validátoru byla opravena.
- **Kompilace:** Microsoft AL Compiler **18.0.41.62505**, dočasný Cloud projekt s runtime **15.0**, bez aplikačních dependencies. Úspěšně zkompilovány přesné AL bloky ze storage reference (Save/Get SecretText) a telemetry reference (Duration → BigInteger → LogMessage). Byl vytvořen `.app`; [výstup](validation/2026-10-23-compiler-compiler-output.txt) a [fingerprint vstupů](validation/2026-10-23-compiler-evidence.json). Reprodukovatelné přes `python scripts/compile-portable-examples.py`; nikam se nepublikuje.

Dva oddělení agenti vygenerovali skutečné odpovědi na stejné tři scénáře: jeden četl jen zachovaný baseline 0.2.0, druhý jen finální sadu. [Původní odpovědi](validation/2026-10-23-baseline-behavior.md), [finální odpovědi](validation/2026-10-23-final-behavior.md). Toto jsou textové behaviorální zkoušky s ručním výběrem podle metadat, ne důkaz automatického skill discovery v hostiteli ani statistický benchmark.

| Scénář | Baseline | Finální sada | Zjištění |
| --- | --- | --- | --- |
| Tooltip, zachovat quoted names/XYZ, Czech fáze později | Malá změna bez dokumentační pipeline | Stejně malá změna, přiměřené diff/build/XLF ověření | Proporcionalita a lokální konvence zachovány; neprokázáno zrychlení. |
| Job Queue, různá field ID, custom transform, úplné klíče, jeden souhrn přes retry | Správný návrh díky povinným integračním opravám vedle vadných originálů | Správný návrh přímo z Job Queue/propagation referencí; žádná vymyšlená signatura, explicitní nejistota doručení | Odstraněna závislost na opravné nadstavbě; zachována důležitá znalost. |
| Review správného subscriber/FlowField kódu | Bez falešného nálezu, ale výslovný rozpor SingleInstance a závislost na wrapperu | Bez nálezu, bez povinného SingleInstance/inherent permissions/FlowField load/rollback/full docs | Konzistentní důvod přímo v používaném obsahu. |

## Původ a udržování

[Provenance JSON](../third-party/al-copilot-skills-collection.json) odděluje `upstreamSha256`, historický `baselineImportedSha256`, lokální baseline a `maintainedFiles`. [Licence a autorství](../THIRD-PARTY-NOTICES.md) jsou zachovány centrálně; všech 39 původních AUTHORS záznamů má přiřazený zdroj. Změny po auditu jsou lokální adaptace, nikoli upstream release.

Po úmyslné úpravě skillu nejprve zkontrolovat obsahový diff, pak spustit `python scripts/record-skill-integrity.py --write` a validátor. Samotné přegenerování hashů neschvaluje význam změny. Při změně struktury je nutné upravit i dispositions a activeSkills; skript to automaticky neobchází. Původní raw hashes se při refreshi nemění.

## Co ověřit před širším firemním použitím

1. **Host discovery:** čerstvá relace Codex a reload VS Code/Copilot mají ukázat právě 29 skillů, bez vyřazených názvů. Ověřit vlastní host verzi a registraci agentů/modelů; simulovaný výběr souborů toto nedokazuje.
2. **Nástroje:** skutečné cílové `app.json`, compiler a dependency symbols; při této práci `al_packages` vrátil prázdný seznam. Čtyři MCP definice jsou konfigurace, ne záruka dostupnosti v každém projektu. ALCops/Node a projektové balíky vyžadují přípravu hosta.
3. **BC sandbox/runtime:** nejsou poskytnuty odpovídající Base/System App symbol packages, test app/runner ani autorizovaný BC test server pro úplné integrační ověření. Proto neproběhlo účtování, upgrade/install, Job Queue restart/concurrency, HTTP bound action, workflow approvals, Dataverse sync, přílohy, report rendering, číselné řady, cenová migrace nebo test oprávnění. Ověřit relevantní případy v pilotním projektu, nikoli předstírat univerzální runtime úspěch.
4. **Překlad:** na konkrétním hostu ověřit izolovaný `al-translator`, dostupný konfigurovaný model a NAB nebo XML-aware cestu. Zachovat placeholders, current `.g.xlf` a pouze cs-CZ. V tomto úkolu překlad ani model routing neběžely.
5. **Externí výsledky:** nebylo ověřeno přijetí business eventu/e-mailu, autentizace uloženým tajemstvím ani Application Insights/KQL data. Kompilace metody tyto výsledky neprokazuje.

## Git a načtení

Změny jsou v pracovním stromu větve `main`, výchozí HEAD `c87c2aa`; žádný commit, push, publikace pluginu ani BC deploy neproběhl. Původní import byl také necommitnutý, takže Git nezobrazí odstranění dříve untracked 39 balíčků jako běžný diff proti HEAD; porovnávací baseline a všech 50 dispozic jsou proto důležité.

Read-only `codex plugin list --marketplace copilot-al-configs --available --json` vrátil lokální **0.3.0 dostupnou, nenainstalovanou a nezapnutou**. Existující junction v uživatelských agent skills ukazuje do tohoto repa; to dokazuje filesystem vazbu, nikoli obnovený katalog běžícího chatu. Pro tuto cestu začít novou relaci. Pro pluginovou cestu nainstalovat/obnovit balíček podporovaným host flow a znovu ověřit discovery. Nekombinovat bez kontroly duplicity obě cesty. VS Code plugin po reloadu musí ukazovat 29 skillů a stávajících 8 agentů; modely jsou provider-specific. Cizí počítače nemají nepushnutý obsah.

Automatická kontrola zamítla mazání starých binárních Word šablon. Vratný přesun do lokální dočasné zálohy mimo repo uspěl; aktivní balíček je neobsahuje. Textové vyřazené soubory byly odstraněny explicitními úpravami. Žádná nedokončená schvalovací žádost nezůstává.
