**Independent behavior evaluation — 2026-10-23**

I discovered the current 29 skills through their filenames and frontmatter name/description, then read the selected instructions and references listed below. I did not read historical audits, consolidation reports, baseline results, or the parent agent's conclusions. These are the assistant responses actually generated for the three supplied scenarios.

**Evidence boundary**

This is a simulated design/review exercise. Filesystem tools were available and actually used to discover/read skills and write this report. No AL edits, builds, deployments, BC operations, or emails were performed. AL/BC tool availability was not probed; I am not claiming that this host lacks those tools. For scenario B, the target BC version, dependency symbols, and runner are unavailable by the scenario's premise. No response below is evidence of compilation, runtime behavior, or tool-host integration.

**A — Generated assistant response**

Minimální změna je nahradit pouze hodnotu vlastnosti existujícího ovládacího prvku `PostingDate`:

```al
ToolTip = 'Explains the posting date.';
```

Ponechám názvy objektů v uvozovkách, příponu `XYZ` i okolní kód. Není důvod přidávat objekt, dokumentaci ani obchodní test kvůli samotnému tooltipu.

Ověření: zkontrolovat diff, sestavit správný projekt podle jeho `app.json` a ověřit nový anglický text ve vygenerovaném `.g.xlf`. Českou synchronizaci a překlad ponechat na samostatnou fázi po požadovaném úspěšném zdrojovém buildu; nyní české XLF neměnit. Výsledek zde představuje návrh změny, build ani překlad jsem v tomto cvičení neprovedl.

Selected skills and references:

- `skills/al-coding-standards/SKILL.md`: preserve project names/affixes and avoid incidental renaming.
- `skills/al-build-validation/SKILL.md`: verify the intended manifest and distinguish build from runtime execution.
- `skills/al-translation-phase/SKILL.md`: English generated-source provenance and separate Czech scope; translation execution is deferred, so no translation worker or host-routing investigation is needed now.
- `skills/al-testing/SKILL.md`: specifically supports source/XLF/build checks for a tooltip-only change instead of synthetic business tests.

**B — Generated assistant response**

Navrhuji trvalý záznam logického běhu s `RunId`, společností, verzí operace, vymezením vstupů, stavem a výsledky jednotlivých položek. Opakované pokusy Job Queue používají stejné `RunId`; nový plánovaný obchodní běh dostane nové. Čítače vycházejí z uložených výsledků, aby opakovaný pokus nepřičetl již dokončenou položku znovu.

1. Zdroj identifikovat alespoň společností, `Document Type` a `No.`; samotné číslo objednávky nestačí. Pracovní položky musí obsahovat také vazbu na skutečnou cílovou fakturu, případně řádek. Předem určit rozsah vstupů a význam změny reference během běhu. Částečná fakturace může vytvořit více cílů; sloučení více zdrojů vyžaduje pravidlo pro rozdílné reference.
2. Zachovat existující transformaci subscriberu a dohledat skutečnou cestu zdroj → případný mezizáznam → faktura → uložení. Rozdílná ID vlastních polí řešit explicitním mapováním, nikoli přečíslováním. `TransferFields` shoduje čísla polí a nenahrazuje vlastní transformaci. Subscriber odstranit či přesunout pouze po prokázání ekvivalentní transformace, validace a pořadí zápisu. Bez symbolů neuvádím konkrétní event ani jeho signaturu.
3. Každou jednotku práce převzít s ochranou proti souběhu, znovu ověřit a provést idempotentně. Obchodní výsledek a stav položky uložit ve stejné transakci, kde to tok dovoluje. Pokud služba sama commitne, obnovovat stav podle trvalého výsledku; vnější transakce tuto mezeru neodstraní. Commit nevkládat dovnitř účtování, které má zůstat atomické. Po dosažení limitu uložit pokračování a naplánovat další úspěšnou dávku ověřeným mechanismem; nastavení retry samo úspěšnou dávku nepokračuje.
4. Po terminálním výsledku všech položek vytvořit v téže databázové transakci právě jeden outbox záznam s unikátním klíčem `(RunId, Summary)`. Odesílat souhrn z něj, nikoli ze subscriberu nebo z každého pokusu. Obchodní dokončení a potvrzení odeslání vést odděleně. Opakované spuštění dokončeného běhu nesmí založit druhý souhrn.
5. Pro odeslání používat stabilní idempotency key a uložit potvrzení poskytovatele, pokud to zvolená cesta podporuje. Po timeoutu s možným přijetím evidovat nejistý stav a výsledek dohledat před opakováním. Samotný příznak `Sent` zapsaný po odeslání nezaručuje jeden e-mail: pád mezi přijetím a zápisem může způsobit duplicitu. Bez spolehlivé deduplikace nebo dohledatelného výsledku nelze současně slíbit právě jeden e-mail a automatické doručení po každém takovém pádu; nejistý případ musí zůstat k vyřešení.

Nejmenší doplnění před implementací:

- Určit, zda job objednávky účtuje, nebo doplňuje již existující faktury, a zda reference patří na hlavičku či řádky. U existujících faktur potvrdit pravidlo změny historické hodnoty a vazbu na zdroj; u kombinovaných dokladů pravidlo konfliktu.
- Získat cílový manifest/verzi a dependency symbols spolu se současným subscriberem a definicemi polí. Pak ověřit přesný publisher, okamžik persistence a podporované plánování Job Queue.
- Určit e-mailovou cestu, příjemce a její možnosti deduplikace/dohledání. Pro následné ověření dodat autorizované testovací prostředí a runner; návrh lze připravit bez nich, úspěšné provedení doložit nelze.

Ověřovací scénáře: různé neprázdné reference a zachovaná transformace po znovunačtení faktury; částečná/vícenásobná fakturace; souběžné spuštění; pád před a po commitu; pád po přijetí e-mailu před lokálním potvrzením; opakování dokončeného běhu; prázdná dávka a přesný limit. Stav Job Queue, uložené obchodní výsledky a potvrzení e-mailu vyhodnotit samostatně. Zde jde o neprovedený návrh, nikoli o otestovanou implementaci.

Selected skills and references:

- `skills/bc-job-queue/SKILL.md` and `references/execution.md`, `references/batching.md`: durable run identity, retries/continuations, background execution, atomic checkpoints, concurrency, uncertain external effects.
- `skills/bc-field-propagation/SKILL.md` and `references/chain-checklist.md`: complete identity, source-to-persistence trace, differing field IDs, existing transformations, partial/combined posting.
- `skills/al-solution-architecture/SKILL.md`: proportional design and unresolved consequential decisions; it does not require a separate architecture document.
- `skills/al-testing/SKILL.md`: targeted regression scenarios and explicit unexecuted-test boundary.

**C — Generated assistant response**

V uvedeném vzoru za zadaných předpokladů nemám nález vyžadující opravu.

- `SingleInstance` není nutné: bezstavový subscriber s `StaticAutomatic`, bez globálních proměnných a bez místního pravidla pro uchování instance je platný. Samotná absence této vlastnosti nedokazuje problém výkonu.
- `InherentPermissions` není povinná vlastnost každého codeunitu. Bez konkrétní chyby oprávnění nebo relevantního pravidla analyzátoru ji nelze požadovat.
- `Balance` nepatří do `SetLoadFields`: jde o FlowField. Načtení normálního pole `Name` přes `SetLoadFields(Name)` a následný výpočet `Balance` přes `CalcFields(Balance)` je za uvedených předpokladů správně.
- Automatický rollback po každém testu nelze předpokládat ani požadovat jako opravu tohoto kódu. Závisí na skutečném runneru a jeho `TestIsolation`; výchozí hodnota je `Disabled`.
- Úplný architektonický dokument ani nová testovací sada nejsou podmínkou přijetí tohoto drobného vzoru.

Zkrácený pseudokód neposuzuji jako úplný zdrojový soubor a nevymýšlím chybějící deklarace či chybnou signaturu. Závěr vychází ze zadaných ověřených deklarací a subscriberu; kompilaci ani běhový test jsem neprovedl.

Selected skills and references:

- `skills/al-bc-solution-review/SKILL.md`: evidence-based findings, no findings quota, proportional review.
- `skills/al-coding-standards/SKILL.md` and `references/subscriber-lifetime.md`: stateless subscriber validity, project policy versus platform requirements, intentional inherent permissions.
- `skills/al-debugging-methodology/references/record-access.md`: directly linked review reference for disputed partial-record/FlowField semantics; the full debugging workflow was unnecessary for a stipulated-correct pattern.
- `skills/al-testing/SKILL.md`: runner isolation is an inspected configuration, not an automatic per-test rollback promise.

No performance or security deep-dive was activated: the scenario supplies no measured cost, reachable access defect, or relevant policy requiring one. No documentation skill was activated because no document-authoring task was requested.
