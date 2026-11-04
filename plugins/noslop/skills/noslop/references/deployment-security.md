# Publication and security — Level 3 (R08)

**Hard stop:** Do not publish, deploy, generate a public URL, expose client data, enable external access, or change publication permissions until the user explicitly authorizes **that publication**.

Before any approved deployment:
1. Confirm intended audience, sensitivity/classification of source material, hosting environment and whether a live deployment is necessary.
2. Jointly select and approve authentication, authorization and access-management controls suitable for the information. Do not presume a shared passcode or noindex equals enterprise security.
3. Obtain specific consent for destination, visibility and access controls; do not infer approval from permission to create the underlying artifact.
4. Protect credentials and secrets, use least privilege, and avoid putting restricted data in public repositories, logs or demo pages.
5. Only then perform the authorized release/deployment and independently validate unauthorized/authorized access, if supported.
6. Report the link and security limitations to the user. Do not expose secret values in a public message or source code.

**Drafting, local execution and private-branch changes are not deployment authorization.** If publication is not approved, stop at a reviewable artifact.
