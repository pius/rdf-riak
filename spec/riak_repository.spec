$:.unshift File.dirname(__FILE__) + "/../lib/"

require 'rdf'
require 'rdf/spec/repository'
require 'rdf/riak'
require 'enumerator'

describe RDF::Riak::Repository do
  context "Riak RDF Repository" do
    before :each do
      @repository = RDF::Riak::Repository.new()
    end
   
    after :each do
      @repository.clear
    end

    # @see lib/rdf/spec/repository.rb in RDF-spec
    it_should_behave_like RDF_Repository
  end

end
