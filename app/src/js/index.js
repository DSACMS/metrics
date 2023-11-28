import { accordion, banner, navigation } from "@uswds/uswds/js"

// This is part of the "uswds-init" machinery to handle failure to load JS
// gracefully. Normally uswds-core/src/js/start.js would do this for us, but
// this file only gets included in bundles - there's no way to individually
// include it.
window.uswdsPresent = true

accordion.on()
banner.on()
navigation.on()