# Current — arrears platform prototype

An interactive prototype of a collections and customer-communication platform for
a UK energy supplier, built as a single self-contained HTML file with no build
step and no dependencies beyond two webfonts.

**[Open the prototype →](https://mosesdex.github.io/current-arrears-prototype/)**

It covers three surfaces, switchable from the top rail:

| Surface | What it is |
|---|---|
| **Agent workspace** | Three panes — queue, conversation, account context. Six cases, each demonstrating a different rule the system has to hold to. |
| **Admin console** | Operations, message routing and failover, workflow gates, template linting, roles and access, import validation, contact rules, audit trail. |
| **Customer app** | Seven screens in a device frame: balance, payment, affordability, Direct Debit, circumstances, messages, dispute. |

Toggle **Design notes** in the top rail to show or hide the annotation layer that
explains the rule behind each decision. Dark mode follows the operating system
and can be overridden.

## Things in here that are deliberate

- **Arrears, never balance.** The two differ whenever an unbilled charge or an
  unapplied payment is in flight, and chasing a balance chases money that is not
  yet owed.
- **Care state sits above the money**, in every panel that shows both. An agent
  who reads the balance first has already framed the conversation.
- **Care states are violet, never red.** Red is the arrears signal in this
  product, and a person needing help is not a risk to be flagged.
- **The composer can be blocked by policy rather than by permission** — a
  disputed balance, a breathing space moratorium, an unconfirmed identity and a
  bereavement each stop sending for a different reason, and the interface says
  which.
- **No agent ranking.** The team table is deliberately unsorted and unscored.
- **No propensity or likelihood-to-pay scoring anywhere**, and no automated
  decision about a person.
- **A per-recipient frequency governor that fails closed.** Send four messages in
  one conversation and it holds the fourth, because mobile operators cap what a
  handset can receive per hour and discard the overflow silently rather than
  returning an error.

## Synthetic data

Every customer, balance, meter reference, conversation and phone number is
invented. Mobile numbers sit inside `07700 900000`–`900999` and the single
landline inside `029 2018 0xxx`, the ranges the regulator reserves for fiction,
so no fixture can collide with a real subscriber. Nothing here is drawn from a
real customer record.

## Running it

There is nothing to install.

```bash
open index.html
```

Any static host will serve it. The file is self-contained apart from Inter,
Newsreader and JetBrains Mono, which load from Google Fonts.

## Scope

This is a prototype for discussion, not a product. It has no backend, no
authentication and no persistence: state lives in the page and resets on reload.
The research and architecture behind it live in a separate repository.

## Licence

MIT — see [LICENSE](LICENSE).
