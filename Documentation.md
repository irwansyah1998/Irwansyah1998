# Portfolio documentation

## Overview

This repository is the GitHub profile repository for Indra Gunawan Ardiansyah. A self-contained, no-build static portfolio lives in [`site/`](site/). Its purpose is to describe professional experience, operational knowledge, skills, public source projects, and future engineering interests with explicit boundaries between verified work and concepts.

## Requirements

- A modern browser with JavaScript enabled for navigation state, filtering, and saved theme preferences. Core content remains readable without JavaScript.
- Python 3 is optional and needed only for the documented local server and validator.
- No npm, Composer, environment variables, or third-party browser requests are required.

## Local development

From the repository root:

```powershell
python -m http.server 4173 --directory site
```

Visit `http://localhost:4173`. HTML and CSS are intentionally kept as static source; there is no compile or bundling step.

Validate local file references and key document contracts:

```powershell
python scripts/validate_site.py
```

## Site architecture

- `site/index.html` owns the content, semantic section structure, project status taxonomy, metadata, diagrams, and link destinations.
- `site/styles.css` provides the tokenized dark/light design system, responsive layout, focus treatment, and reduced-motion behavior.
- `site/script.js` implements theme selection, storage, the mobile menu, project filtering/counts, section indication, and the back-to-top affordance.
- `site/assets/` contains the first-party SVG favicon and social-preview artwork.
- `docs/ARCHITECTURE.md` documents the portfolio implementation and the two referenced application architecture patterns.

No router is needed for a single-page portfolio. The page has no data service or form backend. Project disclosures and architecture diagrams are static, so they cannot silently fail due to a missing API.

## Interaction contracts

- Theme toggle updates `html[data-theme]`, the accessible action label, and browser theme color. It saves only the theme name under `portfolio-theme`; storage errors fall back to page-local behavior.
- Mobile navigation exposes its expanded state, opens by button, closes on Escape, outside click, or link selection, and returns focus on Escape.
- Project filters use the `data-status` attribute on cards; counts are derived from those cards at runtime. Cards remain present in the document when filtered.
- The back-to-top control becomes available after scrolling and uses a normal in-page link.
- Under `prefers-reduced-motion`, transitions and smooth scrolling are minimized.

## Content verification and status policy

- Owner-provided employment, education, operational workflow, and skill context is presented without adding clients, quantified results, or IT responsibilities to the PT AKM role.
- `TugasAkhir` and `SiMadik` source repositories are public. No running deployment was verified. The SiMadik repository carries a custom restrictive license.
- Indra Metered Connection, P2P Chat, and Floating Auto-Tap are labeled with unverified implementation/prototype status. Remaining forward-looking work is labeled research or future concept.
- The operational stock-control story describes an existing spreadsheet-supported workflow, not an already completed enterprise application.
- The CIF concept intentionally does not define a file format.
- Contact is limited to the email address and GitHub profile supplied by the owner; no unverified social accounts or availability claim is published.
- Certificate names, credential IDs, registration numbers, and dates not supplied by the owner are not invented.

## SEO and metadata

The document has a unique title, description, author, Open Graph title/description/PNG image dimensions/alt text, Twitter summary card metadata, language, and favicon. The repository has no verified deployed origin, so it intentionally has no canonical link, production `og:url`, production sitemap, or domain-specific robots rules. The Open Graph artwork is an absolute raw-repository asset URL; it is not a claim that the portfolio itself is live. Revisit metadata if a public domain is configured.

## Deployment

The contents of `site/` are the static production files. Publish that directory as the static host's document root. This repository has no Pages configuration, build workflow, custom domain, or deployment automation. Do not enable hosting until a publishing source and intended public URL have been chosen; then add and test a deployment workflow explicitly.

## Security and privacy

There are no third-party runtime dependencies, credentials, API requests, analytics, or forms. Browser local storage contains only a theme preference. New external links opened in another browsing context set `noopener noreferrer`. The website does not make claims about the security posture of external linked projects.

## Known limitations and next steps

- Real browser rendering, Lighthouse/Core Web Vitals, and assistive-technology testing must be performed against an explicitly chosen browser/device and deployed origin before reporting measured production results.
- The social-preview PNG is rendered from a first-party SVG source; regenerate it if that artwork changes.
- No public website, production URL, live demos, certificate IDs, or project screenshots are available in this repository.
- Revisit long project-card descriptions and architecture diagrams at narrow widths with browser testing before deployment.
- If adding any contact form, first configure a real receiving service and provide success/error behavior and privacy disclosures.

## Change record

See [CHANGELOG.md](CHANGELOG.md) for the current revision summary.
