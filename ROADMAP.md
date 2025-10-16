
1. **Project 1:** Classic model training + deployment pipeline (ECS + CI/CD + Terraform + MLflow).
2. **Project 2:** New dataset + retraining + monitoring + registry + production-grade deployment.

### 🔹 Week 1 (Oct 14–20): Terraform Foundation 

**Goal:** Fully initialize Terraform + remote state + provider ready.

| Day    | Focus                                                                | Outcome                                     |
| ------ | -------------------------------------------------------------------- | ------------------------------------------- |
| Oct 14 | Install Terraform, create `infra/`, set up provider & backend config | `terraform init` works, S3 backend linked   |
| Oct 15 | Create Terraform state bucket (S3) + IAM role for Terraform          | State bucket + permissions verified         |
| Oct 16 | Define VPC, subnets, security groups in Terraform                    | Basic network resources apply cleanly       |
| Oct 17 | Add ECS cluster + task definition skeleton                           | ECS cluster provisioned                     |
| Oct 18 | Add ECR + ALB definitions in Terraform                               | ALB + listener + target group created       |
| Oct 19 | Test `terraform plan` + `apply` from scratch                         | Infra fully spins up                        |
| Oct 20 | Clean up & document infra structure                                  | README: “Terraform Infrastructure Overview” |

---

### 🔹 Week 2 (Oct 21–27): Autoscaling & CloudWatch 

**Goal:** Enable scaling + metrics visualization.

| Day    | Focus                                              | Outcome                      |
| ------ | -------------------------------------------------- | ---------------------------- |
| Oct 21 | Add ECS Service with scaling policies              | Service scales 1–3 tasks     |
| Oct 22 | Connect ALB target group health checks             | ALB → ECS verified           |
| Oct 23 | Create CloudWatch dashboard (CPU, Memory, 4xx/5xx) | Dashboard live               |
| Oct 24 | Add CloudWatch Alarms for CPU/Memory               | Alarms visible in CloudWatch |
| Oct 25 | Test load scaling manually                         | Auto scaling verified        |
| Oct 26 | Terraform outputs + variables cleanup              | Clean reusable infra         |
| Oct 27 | Push infra to GitHub, tag `v1.0-infra`             | Versioned IaC baseline       |

---

### 🔹 Week 3 (Oct 28–Nov 3): Secrets + Retraining 

**Goal:** Secure config + retraining workflow.

| Day    | Focus                                                          | Outcome                                  |
| ------ | -------------------------------------------------------------- | ---------------------------------------- |
| Oct 28 | Create SSM Parameters for secrets (DB creds, MLflow URI, etc.) | Secrets stored securely                  |
| Oct 29 | Update ECS task def to read secrets from SSM                   | Environment variable injection works     |
| Oct 30 | Create retraining script (`retrain.py`)                        | Script logs new run in MLflow            |
| Oct 31 | Add GitHub Actions retrain workflow                            | `train.yml` extended with retraining job |
| Nov 1  | Test manual workflow run                                       | MLflow shows new retrained model         |
| Nov 2  | Add CI artifact uploads to S3                                  | Models versioned                         |
| Nov 3  | Validate whole CI/CD → retrain loop end-to-end                 | Model retrained + artifact tracked     |

---

### 🔹 Week 4 (Nov 4–10): Project 2 Kickoff 

**Goal:** Start 2nd project – new dataset + fresh API.

| Day    | Focus                                          | Outcome                            |
| ------ | ---------------------------------------------- | ---------------------------------- |
| Nov 4  | Choose dataset (structured or image/audio)     | Dataset prepared                   |
| Nov 5  | Write preprocessing + baseline training script | Baseline model working             |
| Nov 6  | Create `mlflow` experiment for new project     | Separate MLflow experiment exists  |
| Nov 7  | Containerize new API service                   | `mlops-api-2` Docker image builds  |
| Nov 8  | Push new API to ECR                            | Image visible in ECR               |
| Nov 9  | Deploy API on ECS                              | Container reachable via ALB        |
| Nov 10 | Write API test (requests-based healthcheck)    | API up and returning predictions |

---

### 🔹 Week 5 (Nov 11–17): Monitoring + Registry 

**Goal:** Model monitoring + registry-driven promotion.

| Day    | Focus                                               | Outcome                           |
| ------ | --------------------------------------------------- | --------------------------------- |
| Nov 11 | Add prediction logging (API → S3 or DynamoDB)       | Data captured for drift detection |
| Nov 12 | Build CloudWatch dashboard for predictions & errors | ML + API metrics visible          |
| Nov 13 | Implement basic drift detection script              | Drift summary in MLflow metrics   |
| Nov 14 | Create MLflow model registry setup                  | Registered models listed          |
| Nov 15 | Add “promote to production” tagging workflow        | Model transitions tracked         |
| Nov 16 | Test retrain → registry → deploy pipeline           | End-to-end verified             |
| Nov 17 | Write README: “Model Lifecycle & Promotion”         | Docs updated                      |

---

### 🔹 Week 6 (Nov 18–24): Canary + Security + Cost (Weeks 12–13)

**Goal:** Production-grade deploys + secure environment.

| Day    | Focus                                       | Outcome                   |
| ------ | ------------------------------------------- | ------------------------- |
| Nov 18 | Implement canary deployment (50/50 traffic) | Canary verified           |
| Nov 19 | Automate rollback on failure                | Canary reverts properly   |
| Nov 20 | Add IAM least privilege review              | Policies refined          |
| Nov 21 | Enable cost explorer + budget alert         | Cost monitoring active    |
| Nov 22 | Set ECS task resource limits                | Costs optimized           |
| Nov 23 | Create CloudWatch alarm for 4xx/5xx spikes  | Proactive alerting        |
| Nov 24 | Wrap up canary + cost governance notes      | Security & FinOps summary |

---

### 🔹 Week 7 (Nov 25–30): Docs + Runbook + Capstone (Weeks 14–16)

**Goal:** Polish everything for portfolio and demo-ready handoff.

| Day    | Focus                                                   | Outcome                 |
| ------ | ------------------------------------------------------- | ----------------------- |
| Nov 25 | Write end-to-end `README.md` with architecture diagrams | Clear project overview  |
| Nov 26 | Add runbook (troubleshooting & recovery steps)          | Ops-ready docs          |
| Nov 27 | Add tests & coverage badges (CI checks)                 | Automated validation    |
| Nov 28 | Record short Loom/video walkthrough                     | Portfolio demo ready    |
| Nov 29 | Review and polish both projects                         | Final tidy-up           |
| Nov 30 | Push final commits + tag `v2.0-final`                   | All goals complete 🎉 |

---
