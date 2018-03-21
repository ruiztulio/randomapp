The RandomApp
===

This app is used as an example for [kubernetes](https://kubernetes.io/) and [Argo](https://github.com/argoproj/argo), to explore and document the posibilities.

The app just stores some random user information in a PostgreSQL database, exposes a frontend where it shows the information and an Json API to query and add some user data.

**NOTE:** Most of the stuff done in the woekflow and kubernetes files are way overkilled for this simple App, but the idea is to have this as a personal reference on how
we can archive some activities using Argo and Kubernetes.