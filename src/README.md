# Healthstack

## Abstract

This page contains the technology specifications for the health information flow (HIF) architecture. The HIF architecture covers mechanisms for consented sharing of personal health information (diagnostic reports, prescriptions, discharge summaries, clinical observations, etc) across different entities as well as those for sharing of non-personal health information. Non-personal health information includes anonymized forms of personal health information and any type of healthcare data which is not obtained from users. When personal health information about a user is shared using the HIF architecture, it leads to the creation of a personal health record (PHR) of the user. The creation and management of PHRs, based on user consent, is one of the main components of the HIF architecture.

## Overview

A Health Information Flow (HIF) is a mechanism of transferring digital health information about users from one organizational entity to another. An entity that generates or collects health information about users and stores it in digital form is referred to as a Health Information Provider (HIP). HIPs could be hospitals, diagnostic labs, pharmacies or other organizations which run software systems to collect, process and store health information of individuals. An entity that seeks health information about users from HIPs is referred to as a Health Information User (HIU). HIUs could be hospitals, insurers, medical research companies and a host of other organizations who are interested in processing health-related information gathered from different sources. A health information flow involves transferring health information from an HIP to an HIU.

Some health information flows involve the transfer of personal information i.e. information which contains personally identifiable information of users or can easily be linked to a single user. We refer to such flows as personal health information flows (personal HIFs). When an HIU aggregates information about a single user from multiple different HIPs using personal HIFs, it leads to the creation of a personal health record (PHR) of the user: a dynamically-generated collection of digital health documents about the user sourced from multiple HIPs. A doctor seeking to treat a patient may ask for health information of that user-generated at different diagnostic labs or hospitals in the past and as such, needs access to a PHR of the user. Many applications require processing aggregate health information about a user and as such, have the need to access the PHR of the user.

HIFs may involve transfer of information that is not personally-identifiable as well. Such information may be non-personal by its very nature (e.g., profile details of a hospital that collects health information of users) or that has been made non-personal by applying anonymization techniques on personal health information. Such HIFs are referred to as non-personal HIFs.

## API documentation

<ul>
    <li>
        <a href="./consent-manager.html">Consent Manager</a>
    </li>
    <li>
        <a href="./gateway.html">Gateway</a>
    </li>
    <li>
        <a href="./health-repository.html">Health Repository</a>
    </li>
</ul>

## Health Information Flows & Technology Specifications

<iframe src="//www.slideshare.net/slideshow/embed_code/key/DUP99kAKROydPS" width="668" height="714" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/ProductNation/health-information-flows-technical-standards-v-05" title="Health Information Flows Technical Standards - V 0.5" target="_blank">Health Information Flows Technical Standards - V 0.5</a> </strong> from <strong><a href="//www.slideshare.net/ProductNation" target="_blank">ProductNation/iSPIRT</a></strong> </div>


## Contributing

[See out github repository to contribute to the website or the specs](https://github.com/iSPIRT/healthstack)