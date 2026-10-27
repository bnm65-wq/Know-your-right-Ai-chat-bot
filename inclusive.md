# Inclusive Language and Accessibility Guide

This guide outlines the core standards for inclusive language, structure, and accessibility in our project documentation. Following these practices ensures our documentation remains clear, welcoming, and accessible to all readers and assistive technologies.

## Heading Structure

* **Single H1:** Each page must have exactly one H1 heading at the beginning, serving as the page title.
* **Sequential Hierarchy:** Subheadings must descend by one level at a time (H1 followed by H2, H2 followed by H3). Do not skip levels (e.g., jumping from H2 to H4).
* **Content Between Headings:** Include introductory prose or a short descriptive paragraph beneath a parent heading before introducing subheadings.

## Inclusive Pronouns

* Use the singular **they** when a subject's gender is unknown or irrelevant. 
* Avoid gendered binary constructions such as "he or she" or "(s)he".

## Inclusive-Language Substitutions

Use industry-standard inclusive terminology across code, comments, and documentation:

| Preferred | Avoid |
| --- | --- |
| allowlist | whitelist |
| blocklist, denylist | blacklist |
| primary, main | master (for branches or controllers) |
| primary, hub, reference | master (general usage) |
| replica, secondary | slave |
| placeholder, sample, mock | dummy |
| smoke testing, confidence testing | sanity check |
| legacy, pre-existing | grandfathered |

## Descriptive Link Text

* Write link text that explicitly describes the destination or context. 
* Avoid ambiguous phrases like "click here" or "this link," which lack context for screen-reader users and search engine scanners.

## Alt Text for Images

* Every informative image must include descriptive alt text summarizing its purpose or content.
* Avoid redundant phrasing like "An image of" or "A screenshot of." Start directly with the subject.
* Mark purely decorative images with empty alt text (`alt=""`) so screen readers skip them.

## Input-Device-Agnostic Language

* Write instructions that apply across input devices (mice, trackpads, touchscreens, keyboards, and assistive technologies).
* Use **select** as the default verb for choosing or activating a UI control rather than device-specific terms like "click," "tap," or "press," unless the documentation specifically details a hardware action or keyboard shortcut.
