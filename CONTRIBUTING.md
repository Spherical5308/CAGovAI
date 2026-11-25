# Contributing to CAGovAI

Thank you for helping. This framework is only useful if it stays accurate as California law and policy change, so corrections from practitioners are the most valuable contributions.

## Ways to contribute
| You want to… | Do this |
|---|---|
| Report a wrong or outdated citation | Open an issue with the **Citation or legal error** template |
| Flag a new law, SAM/SIMM revision, CDT letter or memo | Open an issue with the **Law or policy change** template |
| Ask how to adopt or adapt something | Open an issue with the **Adoption question** template |
| Report something that weakens security or exposes information | Follow [SECURITY.md](./SECURITY.md); do **not** open a public issue |
| Propose wording changes | Open a pull request (below) |

## Ground rules
1. **Cite the source.** Every change that states a legal or policy requirement must name the authority (e.g. "SAM 4986.9(A), rev. 11/2025") and link the official text where one exists. Prefer primary sources: leginfo.legislature.ca.gov, dgs.ca.gov (SAM), cdt.ca.gov (SIMM, Technology Letters, Policy Statements), nist.gov.
2. **Separate requirement from recommendation.** If something goes beyond what law or SAM/SIMM requires, say so in the text (as the Acceptable Use Standard does for P8–P10).
3. **Use the glossary.** Use the terms defined in [GLOSSARY.md](./GLOSSARY.md). If you need a new term, add it there in the same pull request.
4. **Keep it generic.** Use placeholders such as `[State Entity]`. Never add real names, internal system details, completed assessments or other non-public information from any organisation.
5. **Link, don't copy, State forms.** SIMM forms are referenced, not reproduced, so the repository does not go stale when CDT revises them.
6. **Record big decisions.** If a change alters the framework's shape (who decides, what tiers exist, what is in scope), add a short decision record in [docs/adr/](./docs/adr/).
7. **Plain language.** Write for a program manager, not a lawyer. Short sentences, active voice.

## Pull request steps
1. Fork the repository (or create a branch if you have write access).
2. Make your change. If you edit a procedure, check that [PROCEDURE-MAP.md](./PROCEDURE-MAP.md) and the [Authority Crosswalk](./references/Authority-Crosswalk.md) still agree with it. If you edit a form or the inventory, edit the Markdown or CSV and run `python3 scripts/build_office.py` to rebuild the Word and Excel versions (needs `pip install python-docx openpyxl`); never edit the `.docx` or `.xlsx` by hand.
3. Add a line to the `Unreleased` section of [CHANGELOG.md](./CHANGELOG.md).
4. Open a pull request and fill in the template. The link check runs automatically.
5. Resolve every review conversation. The maintainer merges with **Squash and merge**.

## Licensing of contributions
By contributing, you agree that your contribution is licensed under the same terms as the project: [CC BY 4.0](./LICENSE) for documents and [MIT](./LICENSE-CODE) for code. Only contribute material you have the right to license this way. If you adapt third-party material, add its attribution to [NOTICE.md](./NOTICE.md).

## Disclaimer
Contributions are not legal advice, and accepting one does not mean any State Entity or the State of California endorses it.

## Code of Conduct
This project follows the [Contributor Covenant](./CODE_OF_CONDUCT.md).
