/// Related HomiLabs apps on the About screen. Names are store titles, so they are not translated.
const moreApps = [
  (name: 'Lingo15: Learn A Language', package: 'com.homilabs.lingo15'),
  (name: 'IELTS Prep: Mock Test & Bands', package: 'com.homilabs.ielts_simulator'),
  (name: 'TOEFL iBT Prep: Mock Tests', package: 'com.homilabs.toefl_prep'),
  (name: 'Digital SAT Prep: Module Up', package: 'com.homilabs.moduleup'),
];

/// A Play link tagged so Play Console reports installs that came from this app.
String playLink(String package) =>
    'https://play.google.com/store/apps/details?id=$package'
    '&referrer=utm_source%3Dcsca_prep%26utm_medium%3Dapp%26utm_campaign%3Dcrosspromo';
