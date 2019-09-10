DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS agents;

CREATE TABLE agents(
	agent_id serial PRIMARY KEY,  
	first_name varchar(255),
	last_name varchar(255)
);
CREATE TABLE clients(
	client_id serial PRIMARY KEY,  
	agent_id int NOT null REFERENCES agents (agent_id),
	first_name varchar(255),
	last_name varchar(255)
);

INSERT INTO agents(agent_id, first_name, last_name) VALUES (1, 'Chris', 'Fauerbach');
INSERT INTO agents(agent_id, first_name, last_name) VALUES (2, 'Mickey', 'Mouse');

INSERT INTO clients (agent_id, first_name, last_name) VALUES (1, 'Classy', 'Showperson');

SELECT * FROM clients;
SELECT * FROM agents;

SELECT * FROM agents 
    INNER JOIN  clients ON clients.agent_id = agents.agent_id;
	
SELECT * FROM agents 
    LEFT OUTER JOIN  clients ON clients.agent_id = agents.agent_id;

DROP VIEW IF EXISTS agents_with_clients;

CREATE OR REPLACE VIEW agents_with_clients AS
	SELECT agents.agent_id, 
	agents.first_name as agent_first_name,
	agents.last_name as agent_last_name,
	clients.client_id,
	clients.first_name as client_first_name,
	clients.last_name as client_last_name
	FROM agents 
    LEFT OUTER JOIN  clients ON clients.agent_id = agents.agent_id;
	
SELECT * FROM agents_with_clients;

