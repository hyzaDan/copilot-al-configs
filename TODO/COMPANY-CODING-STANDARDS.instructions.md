---
applyTo: '*.al'
---
# Company Coding Standards (AL)

This document defines company-wide rules for AL development. It may be moved to a central web resource in the future. All projects must reference and comply with these standards.

## Object & Field Naming
- All AL object and field names must be no longer than 30 characters.
- Use clear, descriptive names. Avoid abbreviations unless standard.
- Use spaces in object names, do not use underscores.
- Add new object to appropriate folder based on object type
- Do not use project Suffix or WorkspaceSuffix in object or field captions, labels, or translated texts. Suffixes are only for internal identifiers.

## Object & Field Creation
- Use `DataClassification = CustomerContent` for fields containing customer data.

## Table Extensions
- To add triggers to existing fields in table extensions, use the `modify` syntax:
	```al
	modify("Field Name")
	{
		trigger OnAfterValidate()
		begin
			// Your code here
		end;
	}
	```

## Page Extensions
- When adding new fields in page extensions, use `addlast` or `addfirst`. DO NOT USE `addafter` or `addbefore`.
- Use appropriate `ApplicationArea` for the new fields, typically `All`
- Use Rec.Fieldname for field references in page extensions.

## Codeunits
- Example structure:
	```al
	codeunit 4076279 "NSS Core Mgt. WORKSPACESUFFIX"
	{
			Permissions = tabledata "Reservation Entry" = rm, ...;
			// ...procedures...
	}
	```



## Event Subscribers
- When creating an EventSubscriber, find an existing or create a new codeunit object to contain the subscriber.
- The object name should be "ObjectName EH PROJECTSUFFIX", shortened if necessary.
- Example: event from Database::"Standard Customer Sales Code" -> "Std. Cust. Sales Code EH TRT".
- Use the `SingleInstance = true` property for event subscriber codeunits.
- Parameter EventName in subscriber definition must be written without quotes (use plain text, not string literals).

## Permission Sets
- Do not use XML permission sets.
- Use AL `permissionset` objects. For permissions:
	- Name like `*_E*` and caption containing 'Edit' for IMD permissions
	- Name like `*_R*` and caption containing 'Read' for R permissions
	- Name like `*_X*` and caption containing 'Execute' for X permissions
- Add permissions directly to the object, typically in the `PermissionSets` folder.
- Example:
	```al
	permissionset 4076264 "_X WORKSPACESUFFIX"
	{
			Assignable = true;
			Caption = 'NSS Core - Execute', MaxLength = 30;
			Permissions = table "Table Name WORKSPACESUFFIX" = X, 
			...;
	}
	```

## Text & String Handling

### CopyStr Usage
- Use `CopyStr` only if the source and target variable/field lengths differ.
- For truncation, always use `MaxStrLen(destination)` as the third parameter.
- If used in a Get function, use primary key fields from the record variable as the parameter in `MaxStrLen()`.

### Labels & Placeholders
- When using placeholders in labels, add a comment explaining their content:
	```al
	Label 'Some text %1', Comment = '%1 - placeHolderPurpose'
	```
- If using functions like `FieldCaption`, `TableCaption`, specify the object, field, or variable name in the comment.

### Business Central function naming (casing)
- Use PascalCase (also called UpperCamelCase) for Business Central / AL function and method names. That means the first letter of the identifier and each concatenated word is capitalized. Examples: `Insert`, `Modify`, `GetCustomer`, `CalculateTotal`.
- Do not use ALL UPPERCASE for AL/BC function names or method calls. Avoid `INSERT`, `MODIFY`, etc.; use `Insert`, `Modify` instead.

## Enums
- For enum type mismatches, use:
	```al
	Enum::TargetEnum.FromInteger(SourceEnum.AsInteger())
	```

## Translations & Localization
When adding new fields, texts, labels, captions, or tooltips:
1. **Always add translations**
2. **If multiple language files exist**, present the list of available target languages (from existing XLF files or the `Translations` folder) and let the user select which languages to translate
3. **Translation workflow**:
   - Run `al_build` to generate the updated `.g.xlf` file with new translatable texts
   - Use NAB AL Tools to synchronize all XLF files with `refreshXlf` tool
   - Translate the new texts
   - Add or update the `<target>` element with the translated text and set `status="needs-review-translation"`
4. **Available NAB tools for translations**:
   - `refreshXlf` - synchronizes XLF files with generated `.g.xlf`
   - `getTextsToTranslate` - retrieves untranslated texts from XLF file
   - `saveTranslatedTexts` - saves translated texts to XLF file
   - `getTextsByKeyword` - searches for specific texts in XLF file
5. **Translation best practices**:
   - Maintain consistency with existing terminology in the project
   - Keep placeholders (%1, %2, etc.) in the same position and format
   - Preserve formatting and special characters (placeholders, indentation, newlines)
   - Respect character limits indicated by `maxLength` property
   - Technical terms and product names typically remain untranslated
   - Do not use project Suffix in translated texts

## General
- Follow best practices for AL development and code organization.
- Reference this document in all project-specific instructions.
